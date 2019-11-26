import calendar
from collections import deque
import datetime
import itertools
from django import forms

# 캘린더 관련 뷰를 만드는 부품


class BaseCalendarMixin:
    """캘린더 관련 Mixin의 기초 클래스"""
    first_weekday = 0  # 0은 월요일 ~ 6일 일요일
    week_names = ['월', '화', '수', '목', '금', '토', '일']

    def setup_calendar(self):
        """내부 캘린더의 설정처리
        calendar.Calendar클래스의 기능을 활용하기 위해서 인스턴스화.
        Calendar클래스의 monthdatescalendar 메서드는 디폴트가 월요일부터이므로 
        예를 들어 화요일부터 표시하고 싶은 경우(first_weekday=1)에 대응하기 위한 셋업 처리.
        """
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        """first_weekday(최초에 표시되는 요일)에 맞춰 week_names를 바꿈"""
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)  # 리스트 내부 요소를 이동하는 경우 deque사용
        return week_names


class MonthCalendarMixin(BaseCalendarMixin):
    """먼슬리 캘린더 기능을 설정하는 Mixin"""

    def get_previous_month(self, date):
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
        else:
            return date.replace(month=date.month-1, day=1)

    def get_next_month(self, date):
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
        else:
            return date.replace(month=date.month+1, day=1)

    def get_month_days(self, date):
        """해당 월의 모든 날을 주 단위로 리스트에 담아 2차원 리스트 형태로 리턴(n*7 리스트)"""
        return self._calendar.monthdatescalendar(date.year, date.month)

    def get_current_month(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_calendar(self):
        """먼슬리 캘린더 구축에 필요한 dic 리턴"""
        self.setup_calendar()
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            'month_previous': self.get_previous_month(current_month),
            'month_next': self.get_next_month(current_month),
            'week_names': self.get_week_names(),
        }
        return calendar_data


class MonthWithScheduleMixin(MonthCalendarMixin):
    def get_month_schedules(self, start_date, end_date, days):
        lookup = {
            # 예를 들어 date__range: (1일, 31일)를 동적으로 생성
            '{}__range'.format(self.date_field): (start_date, end_date)
        }
        kitchen_id = self.kwargs.get('kitchen_pk')
        # 예를 들어 Reservation.objects.filter(date__range=(1일,31일))
        # 해당 키친을 외래키로 갖고 있으면서 해당 월의 date_field를 갖고 있는 쿼리셋 필터
        queryset = self.model.objects.filter(kitchen_id=kitchen_id, **lookup)

        # days는 month_days로 2차원 리스트
        # day_schedules = {1: [], 2: [] 3: [] ...}
        # day_schedules = {1일의 datetime: 1일의 스케줄 전부, 2일의 datetime: 2일의 스케줄 전부, ...}
        day_schedules = {day: [] for week in days for day in week}
        for schedule in queryset:
            # schedule object에서 date_field 값을 schedule_date에 저장
            # 그 쿼리를 day_schedules[schedule_date]에 append
            schedule_date = getattr(schedule, self.date_field)
            day_schedules[schedule_date].append(schedule)

        size = len(day_schedules)
        return [{key: day_schedules[key] for key in itertools.islice(day_schedules, i, i+7)} for i in range(0, size, 7)]
    """
    [
    {1日: [1日의 모든 스케줄], 2日: [2日의 모든 스케줄].....},  # 1주
    {8日: [8日의 모든 스케줄], 9日: [9日의 모든 스케줄]....},  # 2주
    ...
    {29日: [29日의 모든 스케줄]...},  # 마지막주
    ]
    """

    def get_month_calendar(self):
        calendar_context = super().get_month_calendar()
        month_days = calendar_context['month_days']
        month_first = month_days[0][0]
        month_last = month_days[-1][-1]
        # 기존 context에 month_day_schedules 키 추가
        calendar_context['month_day_schedules'] = self.get_month_schedules(
            month_first,
            month_last,
            month_days,
        )
        return calendar_context
