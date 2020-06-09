import os
import json
import sys
from sparse_arrays import QueryBuilder

if __name__ == "__main__":

    # Loads the strings list stored in the environment (JSON format)
    try:
        strings = json.loads(os.environ.get("SPARSE_ARRAYS_STRINGS"))
    except:
        print("The environment variable is not well defined."
              " Try to instantiate your variable like : "
              " export SPARSE_ARRAYS_STRINGS='[\"your\",\"strings\"]' ")


    # Loads the query list in arguments (only comma separated)
    try:
        query = sys.argv[1].split(",")
    except:
        print("The query argument is not well defined."
              " Try to specify an argument of this form : your,strings,queries")

    # Creates the query builder and do the query
    searcher = QueryBuilder(query, strings)
    print(searcher.search())
