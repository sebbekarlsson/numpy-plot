from corona.parsing.filter import create_filter
from corona.db import DB



db = DB(["corona/indata/cases.json", "corona/indata/vaccine.json"])

db.open()


print(create_filter("cases.date == vaccine.date", db))
