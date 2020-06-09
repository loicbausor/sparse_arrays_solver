import os
import json
from sparse_arrays import QueryBuilder
from flask import Flask
from flask_restplus import Api, Resource


#  Data Loading
## Loads the strings list stored in the environment (JSON format)
try:
    strings = json.loads(os.environ.get("SPARSE_ARRAYS_STRINGS"))
except:
    print("The environment variable is not well defined."
          " Try to instantiate your variable like : "
          " export SPARSE_ARRAYS_STRINGS='[\"your\",\"strings\"]' ")

# API creation
## API body
app = Flask(__name__)
api = Api(app, version='1.0', title='Sparse Arrays API',
          description="This API allows the user to get some aggregated data from the array."
                      " This API is based on the HackerRank Sparse Arrays problem "
                      "(<a href=\"https://www.hackerrank.com/challenges/sparse-arrays/problem\">link</a>).",
          default='Array', default_label='Possible array requests.')


## Array requests
### Array occurrences requests
@api.route('/array/occurrences/<query>', endpoint='occurences', methods=['GET'])
@api.param('query', description="Comma separated strings to search into the array."
                                " Each strings must have a length between 1 and 20 characters."
                                "The number of arguments must not exceed 1000.",
           type='string', _in="body")
class Occurrences(Resource):
    def get(self, query):
        """
         Returns the number of occurrences of the user's queries.
        """
        query = query.split(",")
        searcher = QueryBuilder(query, strings)
        query_result = searcher.search()
        return query_result


if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
