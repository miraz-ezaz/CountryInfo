from django.urls import path
from countries import views


urlpatterns = [
    path('countries/', views.CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('countries/<int:id>/', views.CountryRetrieveUpdateDeleteAPIView.as_view(), name='country-rud'),

    path('countries/region/<str:region_name>/', views.SameRegionCountriesAPIView.as_view(), name='countries-by-region'),
    path('countries/<int:id>/same-region/', views.SameRegionByCountryAPIView.as_view(), name='same-region-by-country'),

]
