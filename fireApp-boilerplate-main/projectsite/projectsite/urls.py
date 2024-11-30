from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, map_incidents, FireStationList, FireStationCreate, FireStationUpdate, FireStationDelete

from fire.views import FireTruckList, FireTruckCreate, FireTruckUpdate, FireTruckDelete
from fire.views import FireFighterList, FireFighterCreate, FireFighterUpdate, FireFighterDelete

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='pie-chart'),
    path('lineChart/', LineCountbyMonth, name='line-chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='multiline-chart'),
    path('multiBarChart/', multipleBarbySeverity, name='multibar-chart'),
    path('stations', map_station, name='map-station'),
    path('incidents', map_incidents, name='map-incidents'),
    
    path('firestation_list', FireStationList.as_view(), name='firestation-list'),
    path('firestation_add', FireStationCreate.as_view(), name='firestation-add'),
    path('firestation_list/<pk>', FireStationUpdate.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete', FireStationDelete.as_view(), name='firestation-delete'),

    path('firetruck_list', FireTruckList.as_view(), name='firetruck-list'),
    path('firetruck_add', FireTruckCreate.as_view(), name='firetruck-add'),
    path('firetruck_list/<pk>', FireTruckUpdate.as_view(), name='firetruck-update'),
    path('firetruck_list/<pk>/delete', FireTruckDelete.as_view(), name='firetruck-delete'),

    path('firefighter_list', FireFighterList.as_view(), name='firefighter-list'),
    path('firefighter_add', FireFighterCreate.as_view(), name='firefighter-add'),
    path('firefighter_list/<pk>', FireFighterUpdate.as_view(), name='firefighter-update'),
    path('firefighter_list/<pk>/delete', FireFighterDelete.as_view(), name='firefighter-delete'),

]
