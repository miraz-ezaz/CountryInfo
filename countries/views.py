from rest_framework import generics, status
from countries.models import Country, Language, Region
from countries.serializers import CountrySerializer


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'


class CountryCreateAPIView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdateAPIView(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'
