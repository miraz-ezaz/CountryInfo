from rest_framework import serializers
from countries.models import Country, Currency, Language, Region, Subregion, Timezone, TopLevelDomain, Capital, LatLng


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code', 'name', 'symbol']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['code', 'name']


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ['name']


class TLDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopLevelDomain
        fields = ['name']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']


class SubregionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subregion
        fields = ['name', 'region']


class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = ['name', 'latitude', 'longitude']


class LatLngSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLng
        fields = ['latitude', 'longitude']


class CountrySerializer(serializers.ModelSerializer):
    currencies = CurrencySerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    timezones = TimezoneSerializer(many=True, read_only=True)
    tlds = TLDSerializer(many=True, read_only=True)
    region = RegionSerializer(read_only=True)
    subregion = SubregionSerializer(read_only=True)
    capitals = CapitalSerializer(many=True, read_only=True)
    latlng = LatLngSerializer(read_only=True)
    borders = serializers.SlugRelatedField(many=True, slug_field='cca3', read_only=True)

    class Meta:
        model = Country
        fields = '__all__'
