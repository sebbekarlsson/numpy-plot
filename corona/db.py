import pathlib
import json
from functools import reduce


# corona/indata/cases.json => "cases"
clean_name = lambda x: pathlib.Path(x).name.replace('.json', '')


class DB(object):


    def __init__(self, filenames):
        self.filenames = filenames
        self.data = {}

    # self.filenames => {
    #    "cases": [...],
    #    "vaccine": [...],
    # }
    def create_initial_data(self):
        column_names = list(map(clean_name, self.filenames))
        return reduce(lambda a, b: {**a, b: []}, column_names, {})

    # 1. exec self.data = self.create_initial_dat
    # 2. data["cases"] = en lista med case dictionaries fran filen
    # 3. data["vaccine"] = en lista med vaccine dictionaries fran filen
    def open(self):
       self.data = self.create_initial_data()

       for filepath in self.filenames:
           name = clean_name(filepath)
           self.data[name] = json.load(open(filepath)).get('records')

    # returnerar vardet fran self.data[name],
    # och mappar om listan dar i till en lista med modeller (vara klasser)
    def get(self, name, clazz):
        return map(clazz.from_dict, self.data.get(name))
