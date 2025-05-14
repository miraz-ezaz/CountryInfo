from django.urls import path
from countries import views


urlpatterns = [
    path('countries/', views.CountryListView.as_view(), name='country-web-list'),
    path('countries/<int:pk>/', views.CountryDetailView.as_view(), name='country-web-detail'),
]
