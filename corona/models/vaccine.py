import datetime


class Vaccine(object):

    def __init__(
        self,
        date: datetime.date,
        first_dose: int,
        first_dose_refused: int,
        second_dose: int,
        unknown_dose: int,
        doses_received: int,
        region: str,
        population: int,
        country: str,
        target_group: str,
        name: str,
        denominator: int
    ):
       self.date = date
       self.first_dose = first_dose
       self.first_dose_refused = first_dose_refused
       self.second_dose = second_dose
       self.unknown_dose = unknown_dose
       self.doses_received = doses_received
       self.region = region
       self.population = population
       self.country = country
       self.target_group = target_group
       self.name = name
       self.denominator = denominator


    @staticmethod
    def from_dict(obj: dict):
        return Vaccine(
            date=datetime.datetime.strptime(obj.get('YearWeekISO') + '-1', "%Y-W%W-%w"),
            first_dose=int(obj.get('FirstDose') or 0),
            first_dose_refused=int(obj.get('FirstDoseRefused') or 0),
            second_dose=int(obj.get('SecondDose') or 0),
            unknown_dose=int(obj.get('UnknownDose') or 0),
            doses_received=int(obj.get('NumberDosesReceived') or 0),
            region=obj.get('Region'),
            population=int(obj.get('Population') or 0),
            country=obj.get('ReportingCountry'),
            target_group=obj.get('TargetGroup'),
            name=obj.get('Vaccine'),
            denominator=int(obj.get('Denominator') or 0)
        )
