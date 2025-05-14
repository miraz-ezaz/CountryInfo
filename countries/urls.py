from django.urls import path
from countries import views


urlpatterns = [
    path('countries/', views.CountryListAPIView.as_view(), name='country-list'),
    path('countries/<int:id>/', views.CountryDetailAPIView.as_view(), name='country-detail'),

]
