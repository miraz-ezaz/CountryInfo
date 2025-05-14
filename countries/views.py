from rest_framework import generics, status
from countries.models import Country, Language, Region
from countries.serializers import CountrySerializer


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


