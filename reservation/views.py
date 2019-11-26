from django.shortcuts import render
from .models import Kitchen_info, Reservation
import folium
import branca
from folium.plugins import MarkerCluster


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
                           '</h1><br>주소: <br>사진</div>', script=True)
        iframe = folium.IFrame(html=html, width=300, height=300)
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


def kitchen_detail(request, kitchen_pk):
    kitchen = Kitchen_info.objects.get(pk=kitchen_pk)
    return render(request, 'reservation/kitchen_detail.html', {'kitchen': kitchen})
