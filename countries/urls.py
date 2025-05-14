from django.urls import path
from countries import views


urlpatterns = [
    path('', views.CountryListView.as_view(), name='country-web-list'),
    path('<int:pk>/', views.CountryDetailView.as_view(), name='country-web-detail'),
]
