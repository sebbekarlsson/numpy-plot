from corona.parsing.filter import create_filter



class Query(object):


    def __init__(self, db, lazy_result=None):
        self.db = db
        self.lazy_result = lazy_result

    def results(self):
        return self.lazy_result

    def create_filter(self, query_str):
        return create_filter(query_str, self.db)

    def where(self, query_str: str):
        return Query(self.db, self.create_filter(query_str))
