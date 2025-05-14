from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.db.models import Q

from countries.models import Country, Language, Region
from countries.serializers import CountrySerializer


# List & Create
class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


# Retrieve, Update & Delete
class CountryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'


class CountryDeleteAPIView(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'


class SameRegionCountriesAPIView(APIView):
    def get(self, request, region_name):
        countries = Country.objects.filter(region__name__iexact=region_name)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class SameRegionByCountryAPIView(APIView):
    def get(self, request, id):
        country = get_object_or_404(Country, id=id)
        region = country.region
        if not region:
            return Response({"message": "This country has no region data."}, status=404)

        countries = Country.objects.filter(region=region).exclude(id=country.id)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class CountriesByLanguageAPIView(APIView):
    def get(self, request, lang_code):
        countries = Country.objects.filter(languages__code__iexact=lang_code)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class CountrySearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        countries = Country.objects.filter(
            Q(name_common__icontains=query) | Q(name_official__icontains=query)
        )
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)