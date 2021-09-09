# db.get("cases").where("cases.date == vaccines.date")


# Rack upp handen nar ni har en query klass som ser ut sa har,
# samt skapat en "parser.py" fil.

class Query(object):


    def __init__(self, db, lazy_result):
        self.db = db
        self.lazy_result = lazy_result

    def create_filter(self, query_str):
        '''
        1. Parse query_str
        2. Return a lambda that represents the query
        '''
        pass

    def where(self, query_str: str) -> Query:
        return Query(sef.db, filter(self.create_filter(query_str), self.lazy_results))
