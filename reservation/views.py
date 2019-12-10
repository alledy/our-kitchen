from django.shortcuts import render, redirect
from django.views import generic
from . import mixins
from .forms import ReservationForm
from .models import Kitchen_info, Reservation
import folium
from folium.plugins import MarkerCluster
import datetime


def index(request):
    kitchens = Kitchen_info.objects.all()
    # Get first data

    m = folium.Map(
        location=[37.558773, 126.970260],
        zoom_start=11,
    )

    marker_cluster = MarkerCluster().add_to(m)

    for i in kitchens:
        html = folium.Html('<div style="font-family: Nanum Gothic"><h1>' + i.kitchen_name +
                           '</h1>', script=True)
        iframe = folium.IFrame(html=html, width=200, height=100)
        popup = folium.Popup(iframe, parse_html=True)
        tooltip = i.kitchen_name
        folium.Marker(
            location=[i.lat, i.lng],
            popup=popup,
            icon=folium.Icon(color="red", icon="ok"),
            tooltip=tooltip,
        ).add_to(marker_cluster)

    m.save('reservation/map.html')
    return render(request, 'reservation/index.html', {'map': m._repr_html_, 'kitchens': kitchens})


# def detail(request, kitchen_pk):
#     kitchen = Kitchen_info.objects.get(pk=kitchen_pk)
#     return render(request, 'reservation/detail.html', {'kitchen': kitchen})


class MonthCalendar(mixins.MonthWithScheduleMixin, generic.CreateView):
    template_name = 'reservation/reservation.html'
    model = Reservation
    date_field = 'start_date'
    form_class = ReservationForm

    # 폼클래스에 url parameter 넘기기 위해 사용
    def get_form_kwargs(self):
        kwargs = super(MonthCalendar, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    # def get_queryset(self):
    #     kitchen_pk = self.kwargs['kitchen_pk']
    #     kitchen = Reservation.objects.get(kitchen_id=kitchen_pk)
    #     current_cap = kitchen.capacity
    #     kitchen.capacity = current_cap - 1

    def get_context_data(self, **kwargs):
        kitchen_pk = self.kwargs['kitchen_pk']
        kitchen = Kitchen_info.objects.get(pk=kitchen_pk)

        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        # 이 부분 고치기
        calendar_context.update({'kitchen': kitchen})
        context.update(calendar_context)
        return context

    def form_valid(self, form):
        kitchen_pk = self.kwargs['kitchen_pk']
        # url param이 없는 경우도 존재하므로 get으로 값을 가져와야 함
        # 안 그러면 에러
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        if year and month:
            pass
        else:
            date = datetime.date.today()
            year = date.year
            month = date.month

        kitchen = Kitchen_info.objects.get(pk=kitchen_pk)
        reservation = form.save(commit=False)
        reservation.kitchen = kitchen
        reservation.save()
        return redirect('reserve:reservation', kitchen_pk=kitchen_pk, year=year, month=month)
