from django.urls import path
from countries import views


urlpatterns = [
    path('countries/', views.CountryListAPIView.as_view(), name='country-list'),
    path('countries/<int:id>/', views.CountryDetailAPIView.as_view(), name='country-detail'),
    path('countries/create/', views.CountryCreateAPIView.as_view(), name='country-create'),
    path('countries/<int:id>/update/', views.CountryUpdateAPIView.as_view(), name='country-update'),
    path('countries/<int:id>/delete/', views.CountryDeleteAPIView.as_view(), name='country-delete'),

]
