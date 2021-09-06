from corona.db import DB
from corona.models.case import Case
from corona.models.vaccine import Vaccine


db = DB(["corona/indata/cases.json", "corona/indata/vaccine.json"])

db.open()

cases = db.get('cases', Case)
vaccine = db.get('vaccine', Vaccine)


for case in cases:
    print(case.date)
