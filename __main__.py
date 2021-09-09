from corona.db import DB
from corona.models.case import Case
from corona.models.vaccine import Vaccine
from corona.query import Query


db = DB(["corona/indata/cases.json", "corona/indata/vaccine.json"])

db.open()


q = Query(db).where("cases.date == vaccine.date")


for case in q.results():
    print(case.__dict__)

# cases = db.get('cases', Case)
# vaccine = db.get('vaccine', Vaccine)


# for case in cases:
#     print(case.__dict__)
