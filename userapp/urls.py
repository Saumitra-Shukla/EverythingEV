from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from userapp.views import (ChargingStationProviderListView, ChargingStationProviderDeleteView, MaintenanceMan,
                           SearchListView)

# ChargingStation - CS
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('registerConsumer/', views.registerConsumer, name='registerConsumer'),
    path('registerConsumerSocial/', views.registerConsumerSocial, name='registerConsumerSocial'),
    path('registerProvider/', views.registerProvider, name='registerProvider'),
    path("UpdateProfile/", views.UpdateProfile, name='UpdateProfile'),
    path('Charging-Station/', views.CS, name='Charging-Station'),
    path('Charging-Station/add/', views.AddChargingStation, name='AddChargingStation'),
    path('Charging-Station/my-stations/', ChargingStationProviderListView.as_view(), name='Charging-Station-PLV'),
    path('Charging-Station/analytics/<int:pk>', views.ChargingStationAnalytics, name='Charging-Station-Analytics'),
    path('Charging-Station/dashboard/<int:pk>', views.ChargingStationDashboard, name='Charging-Station-Dashboard'),
    path('station/<int:pk>/delete/', ChargingStationProviderDeleteView.as_view(), name='DeleteStation'),
    path('Charging-Station/all-stations/', views.ChargingStationConsumer, name='Charging-Station-CLV'),
    path('Charge-Pooling/', views.ChargePooling, name='Charge-Pooling'),
    path('Route-Your-Way/', views.RouteYourWay, name='Route-Your-Way'),
    path('registerMaintenance/', MaintenanceMan.as_view(), name="registerMaintenance"),
    path('Maintenance-man/dashboard', views.MaintenanceDashboard, name='Maintenance-man-dashboard'),
    path('Maintenance-man/view-all', SearchListView.as_view(), name='All-Maintenance-Man'),
    path('Maintenance-man/complaints', views.MaintenanceComplaint, name='Complaint-Dashboard'),
    path('book/<int:pk>', views.bookMaintenanceMan, name="bookingMm"),
    path('faq/',views.faq, name="faq")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
