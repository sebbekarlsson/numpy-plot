import datetime


class Case(object):


    def __init__(
        self,
        date: datetime.date,
        day: int,
        month: int,
        year: int,
        cases: int,
        deaths: int,
        country: str,
        geoid: str,
        country_terr_code: str,
        population: int,
        continent: str
    ):
        self.date = date
        self.day = day
        self.month = month
        self.year = year
        self.cases = cases
        self.deaths = deaths
        self.country = country
        self.geoid = geoid
        self.country_terr_code = country_terr_code
        self.population = population
        self.continent = continent

    @staticmethod
    def from_dict(obj: dict):
        return Case(
            date=datetime.datetime.strptime(obj.get('dateRep'), '%d/%m/%Y'),
            day=int(obj.get('day', 0)),
            month=int(obj.get('month', 0)),
            year=int(obj.get('year', 0)),
            cases=int(obj.get('cases', 0)),
            deaths=int(obj.get('deaths', 0)),
            country=obj.get('countriesAndTerritories'),
            geoid=obj.get('geoId'),
            country_terr_code=obj.get('countryterritoryCode'),
            population=int(obj.get('popData2020')),
            continent=obj.get('continentExp')
        )
