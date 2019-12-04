# our-kitchen

## Overview
공유 주방의 예약 관리, 상권 분석, 챗봇 상담 기능을 장고(Django)로 구현한 웹 어플리케이션입니다. 
![image](https://user-images.githubusercontent.com/46309894/70120714-8b93dd00-16b0-11ea-8bf4-b4c241072dd7.png)

### 예약 관리
- 공유 주방의 위치를 마커로 표시합니다. 
- 예약을 원하는 공유 주방을 클릭하면 해당 공유 주방의 스케줄이 표시된 달력 페이지로 이동합니다.
- 달력에서 공유 주방의 예약 현황을 확인할 수 있으며, 시간대와 기간(3개월 이상)을 선택한 후 예약을 진행할 수 있습니다. 
![OurKitchen_2](https://user-images.githubusercontent.com/46309894/70120835-c6961080-16b0-11ea-8943-53e1c91c53ef.png)
![OurKitchen_3](https://user-images.githubusercontent.com/46309894/70120842-ca299780-16b0-11ea-8f4e-334e2857c095.png)

### 상권 분석
- 어느 위치의 공유 주방을 선택하면 좋을지 주변 상권 분석을 통해 알려줍니다.
- 해당 공유 주방의 마커를 클릭하면 [소상공인 상가(상권) 정보 API](https://www.data.go.kr/dataset/15012005/openapi.do)를 통해 데이터를 받아 주변 음식점 정보 및 창업 지수 등을 시각화합니다. 
![OurKitchen_4](https://user-images.githubusercontent.com/46309894/70120852-cc8bf180-16b0-11ea-9178-452569087edd.png)

### 챗봇 상담
- 공유 주방 입점에 대하여 상담이 필요하면 챗봇에게 상담을 예약할 수 있습니다.
- 상담 요청 내역과 승인 여부는 마이페이지에서 확인할 수 있습니다. 
![OurKitchen_5](https://user-images.githubusercontent.com/46309894/70121415-dd893280-16b1-11ea-9eec-d3c5056b7ca4.png)
![OurKitchen_6](https://user-images.githubusercontent.com/46309894/70122039-360cff80-16b3-11ea-941b-ab28482ad195.png)

## Skills
- 웹 프레임워크: Django
- DB: SQLite3
- 시각화 라이브러리: Folium, Leaflet, Chart.js
- 챗봇: Dialogflow(Line)
- 스타일: Twitter Bootstrap
