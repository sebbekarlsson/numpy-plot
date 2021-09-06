import pytest
from corona.db import DB
from corona.models.case import Case
from corona.models.vaccine import Vaccine


def test_get_cases():
    db = DB([
        "corona/tests/indata/cases.json",
        "corona/tests/indata/vaccine.json"
    ])

    db.open()

    cases = list(db.get("cases", Case))
    assert len(cases)

    assert cases


def test_get_vaccine():
    db = DB([
        "corona/tests/indata/cases.json",
        "corona/tests/indata/vaccine.json"
    ])

    db.open()

    vaccines = list(db.get("vaccine", Vaccine))
    assert len(vaccines)

    assert vaccines
