class QueryBuilder:
    def __init__(self, query, strings):
        """Constructor of the class. Creates the attributes of the class and checks
         if the constraints are respected.
        Inputs :
            :query: A list containing strings. Corresponds to the query the user wants to do.
                    This arguments must match the constraints of the SparseArray problem (see doc).
            :strings: A list containing strings. Corresponds to the array the user wants to search into.
                    This arguments must match the constraints of the SparseArray problem (see doc).
        """

        # Checks if the constraints are respected for the two inputs
        for arg_name, arg_value in {"query": query, "strings": strings}.items():
            # List type constraint
            if not isinstance(arg_value, (list, tuple)):
                raise TypeError("The argument " + arg_name + " has type " + str(type(arg_value)) + "."
                                + " List or tuple was expected.")
            if not 1 <= len(arg_value) <= 1000:
                raise TypeError("The argument " + arg_name + " has length " + str(len(arg_value)) + "."
                                + " Expected a length between 1 and 1000.")

            for i in range(len(arg_value)):
                # String type constraint
                if type(arg_value[i]) is not str:
                    raise TypeError("Index " + str(i) + " of " + arg_name
                                    + " has type " + str(type(arg_value[i])) + "."
                                    + " String was expected.")
                # Length of the strings constraint
                if not 1 <= len(arg_value[i]) <= 20:
                    raise ValueError("Index " + str(i) + " of " + arg_name
                                     + " has " + str(len(arg_value[i])) + " characters."
                                     + " Expected a length between 1 and 20.")


        # Set the attributes
        self.query = query
        self.strings = strings

    def search(self):

        """Searches for the number of occurrences of each strings of the query in the strings attribute.
        Returns :
            :query_result: A dictionary like {string_query : string_occurrence}
        """

        query_results = dict()

        for q in self.query:
            # Computes the number of occurrence of the query q in the input collection
            occurrence = self.strings.count(q)
            query_results[q] = occurrence

        return query_results
