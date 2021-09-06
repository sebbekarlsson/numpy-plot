import pytest
from corona.models.case import Case
import datetime


TEST_DATA = [
    {
         "dateRep" : "02/09/2021",
         "day" : "02",
         "month" : "09",
         "year" : "2021",
         "cases" : 1821,
         "deaths" : 6,
         "countriesAndTerritories" : "Austria",
         "geoId" : "AT",
         "countryterritoryCode" : "AUT",
         "popData2020" : "8901064",
         "continentExp" : "Europe"
      },
      {
         "dateRep" : "01/09/2021",
         "day" : "01",
         "month" : "09",
         "year" : "2021",
         "cases" : 1265,
         "deaths" : 1,
         "countriesAndTerritories" : "Austria",
         "geoId" : "AT",
         "countryterritoryCode" : "AUT",
         "popData2020" : "8901064",
         "continentExp" : "Europe"
      }
]


def test_from_dict_single():
    dict_in = TEST_DATA[0]

    case = Case.from_dict(dict_in)

    assert case
    assert case.date
    assert isinstance(case.date, datetime.date)

# bra att veta att man kan gora sa har
# @pytest.mark.parametrize("test_input,expected", [(TEST_DATA[i], EXPECTED_DATA[i]) for i in range(2)])
# def test_from_dict(test_input, expected):
#     c = Case.from_dict(test_input)
#     assert c.__dict__ is expected.__dict__
