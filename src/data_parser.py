def get_duplicate_count(input_strings: str) -> str:
    """
    This method parses the input string, check
    duplicate character and count how many time the
    the duplicate character appears.

    :param input_strings: The string only accept character
                          "A", "B", "C", "D"
    :returns: duplicate character and appearance count
    .. note:: We will not raise an exception, caller
              should check the return code.
              If None is returned, the input string is not valid.
    """
    if len(input_strings) == 0:
        print("Input data is empty")
        return ""

    if input_strings.count(" ") > 0 or not input_strings.isalpha():
        print(f"Input data is not valid {input_strings}")
        return None

    return_string: str = ""
    lookup_lists = []
    temp = None
    counter = 0
    accept_character_list = ["A", "B", "C", "D"]

    for this_char in input_strings:
        if this_char not in accept_character_list:
            print(f"Input data is empty")
            return None

        if not temp:
            temp = this_char

        if this_char == temp:
            counter += 1

        if this_char != temp:
            lookup_lists.append((temp, counter))
            return_string = return_string + temp + str(counter)
            temp = this_char
            counter = 1

    lookup_lists.append((this_char, counter))
    return_string = return_string + temp + str(counter)
    print(lookup_lists)

    return return_string
