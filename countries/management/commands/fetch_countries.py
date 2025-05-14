import requests
from django.core.management.base import BaseCommand
from countries.models import (
    Country, Region, Subregion, Currency, Language,
    Timezone, TopLevelDomain, LatLng, Capital
)


class Command(BaseCommand):
    help = 'Fetch country data from restcountries.com and populate the database'

    def handle(self, *args, **kwargs):
        url = 'https://restcountries.com/v3.1/all'
        response = requests.get(url)
        if response.status_code != 200:
            self.stderr.write("Failed to fetch data.")
            return

        data = response.json()
        self.stdout.write(f"Fetched {len(data)} countries.")

        cca3_country_map = {}

        for index, item in enumerate(data, 1):
            name_common = item['name']['common']
            name_official = item['name']['official']
            cca2 = item.get('cca2', '')
            cca3 = item.get('cca3', '')
            ccn3 = item.get('ccn3')
            cioc = item.get('cioc')
            independent = item.get('independent', False)
            status = item.get('status')
            un_member = item.get('unMember', False)
            fifa = item.get('fifa')
            population = item.get('population', 0)
            area = item.get('area', 0.0)
            landlocked = item.get('landlocked', False)
            flag_emoji = item.get('flag')
            flag_alt = item.get('flags', {}).get('alt')
            flag_png = item.get('flags', {}).get('png')
            flag_svg = item.get('flags', {}).get('svg')
            start_of_week = item.get('startOfWeek')
            map_google = item.get('maps', {}).get('googleMaps')
            map_open = item.get('maps', {}).get('openStreetMaps')
            continents = ", ".join(item.get('continents', []))

            region_name = item.get('region')
            subregion_name = item.get('subregion')

            region = Region.objects.get_or_create(name=region_name)[0] if region_name else None
            subregion = Subregion.objects.get_or_create(name=subregion_name, region=region)[0] if subregion_name and region else None

            country, _ = Country.objects.update_or_create(
                cca3=cca3,
                defaults={
                    "name_common": name_common,
                    "name_official": name_official,
                    "cca2": cca2,
                    "ccn3": ccn3,
                    "cioc": cioc,
                    "independent": independent,
                    "status": status,
                    "un_member": un_member,
                    "fifa": fifa,
                    "region": region,
                    "subregion": subregion,
                    "population": population,
                    "area": area,
                    "landlocked": landlocked,
                    "flag_emoji": flag_emoji,
                    "flag_alt": flag_alt,
                    "flag_png": flag_png,
                    "flag_svg": flag_svg,
                    "start_of_week": start_of_week,
                    "map_google": map_google,
                    "map_openstreet": map_open,
                    "continents": continents,
                }
            )

            country.currencies.clear()
            country.languages.clear()
            country.timezones.clear()
            country.tlds.clear()
            country.borders.clear()

            cca3_country_map[cca3] = country

            self.stdout.write(f"[{index}/{len(data)}] Added: {name_common} ({cca3})")

            country.capitals.all().delete()
            for cap in item.get("capital", []):
                Capital.objects.create(
                    country=country,
                    name=cap,
                    latitude=item.get("capitalInfo", {}).get("latlng", [None, None])[0],
                    longitude=item.get("capitalInfo", {}).get("latlng", [None, None])[1],
                )

            latlng = item.get("latlng")
            if latlng and len(latlng) == 2:
                LatLng.objects.update_or_create(
                    country=country,
                    defaults={"latitude": latlng[0], "longitude": latlng[1]}
                )

            for code, details in item.get("currencies", {}).items():
                currency, _ = Currency.objects.get_or_create(
                    code=code,
                    defaults={"name": details.get("name", ""), "symbol": details.get("symbol", "")}
                )
                country.currencies.add(currency)

            for code, name in item.get("languages", {}).items():
                language, _ = Language.objects.get_or_create(code=code, defaults={"name": name})
                country.languages.add(language)

            for tz in item.get("timezones", []):
                timezone, _ = Timezone.objects.get_or_create(name=tz)
                country.timezones.add(timezone)

            for tld in item.get("tld", []):
                domain, _ = TopLevelDomain.objects.get_or_create(name=tld)
                country.tlds.add(domain)

        for item in data:
            country = cca3_country_map.get(item.get('cca3'))
            if not country:
                continue
            for border_code in item.get('borders', []):
                border_country = cca3_country_map.get(border_code)
                if border_country and border_country != country:
                    country.borders.add(border_country)

        self.stdout.write("Data import complete.")
