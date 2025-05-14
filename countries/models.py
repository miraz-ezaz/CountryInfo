from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Subregion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, related_name='subregions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Timezone(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TopLevelDomain(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name_common = models.CharField(max_length=255)
    name_official = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=3)
    cca3 = models.CharField(max_length=3)
    ccn3 = models.CharField(max_length=10, null=True, blank=True)
    cioc = models.CharField(max_length=10, null=True, blank=True)
    independent = models.BooleanField(default=False)
    status = models.CharField(max_length=100, null=True, blank=True)
    un_member = models.BooleanField(default=False)
    fifa = models.CharField(max_length=10, null=True, blank=True)

    region = models.ForeignKey(Region, related_name='countries', on_delete=models.SET_NULL, null=True)
    subregion = models.ForeignKey(Subregion, related_name='countries', on_delete=models.SET_NULL, null=True)

    population = models.BigIntegerField()
    area = models.FloatField()
    landlocked = models.BooleanField(default=False)

    flag_emoji = models.CharField(max_length=10, null=True, blank=True)
    flag_png = models.URLField(null=True, blank=True)
    flag_svg = models.URLField(null=True, blank=True)
    flag_alt = models.TextField(null=True, blank=True)

    start_of_week = models.CharField(max_length=20, null=True, blank=True)
    map_google = models.URLField(null=True, blank=True)
    map_openstreet = models.URLField(null=True, blank=True)
    continents = models.CharField(max_length=100, null=True, blank=True)

    currencies = models.ManyToManyField(Currency, related_name='countries', blank=True)
    languages = models.ManyToManyField(Language, related_name='countries', blank=True)
    timezones = models.ManyToManyField(Timezone, related_name='countries', blank=True)
    tlds = models.ManyToManyField(TopLevelDomain, related_name='countries', blank=True)
    borders = models.ManyToManyField("self", symmetrical=True, blank=True)

    def __str__(self):
        return self.name_common


class Capital(models.Model):
    country = models.ForeignKey(Country, related_name='capitals', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.country.cca2})"


class LatLng(models.Model):
    country = models.OneToOneField(Country, related_name='latlng', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"

