from django.shortcuts import render
import folium

from app.models import Marker

def mapa(request):

    m = folium.Map(location=(-10.441649, -45.162299), zoom_start=15)


    for marker in Marker.objects.all():
        kw = {"prefix": "fa", "color": marker.cor, "icon": marker.icone}

        icon = folium.Icon(**kw)
        folium.Marker(
            location=[marker.latitude, marker.longitude],
            icon=icon,
            tooltip=str(marker.nome)
        ).add_to(m)

    folium.GeoJson(
        (open("rotas/rota01.geojson").read()),
        style_function= lambda x: {"color": "blue"},
        name="Rota de Ida"
        ).add_to(m)
    folium.GeoJson(
        (open("rotas/rota02.geojson").read()),
        style_function= lambda x: {"color": "red"},
        name="Rota de Chegada"
        ).add_to(m)

    return render(
        request,
        'app/index.html',
        {
            'mapa': m._repr_html_()
        }
    )
