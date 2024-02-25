

class JustForFunUtil:

    def flatten_the_dict(self, simple_dict):
        """
        Flatens the dict such that if a nested dict is given
        , no matter how many levels of nesting is present. It recursively
        flatens the dict all in single level.
        """
        ans_dict = {}

        def flatten_dict(parent_key, dict_val):
            for child_key, value in dict_val.items():
                if isinstance(value, dict):
                    flatten_dict(parent_key+"_"+child_key, value)
                else:
                    ans_dict[parent_key+"_"+child_key] = value
            return

        flatten_dict("", simple_dict)

        return ans_dict