#DEFINE THE STRING FUNCTION
def fun2(input_string):
    #CREATE A DICTIONARY TO STORE THE COUNTS OF LETTERS OR DIGITS
    count_dict = {}

    #ITERATE THROUGH THE CHARACTERS IN THE INPUT STRING
    for char in input_string:
        #CHECK IF THE CHARACTER IS A LETTER OR A DIGIT
        if char.isalnum():
            #CONVERT THE CHARACTER TO LOWER CASE
            char = char.lower()
            #GET THE COUNT INCREMENT OR INCREASE IN THE DICTIONARY
            count_dict[char] = count_dict.get(char, 0) + 1

    #IF THERE ARE NO LETTERS OR DIGITS FOUND, RETURN NONE
    if not count_dict:
        return None

    #FIND THE MOST FREQUENT LETTERS OR DIGITS
    max_freq = max(count_dict.values())
    most_frequent_chars = [char for char, freq in count_dict.items() if freq == max_freq]

    #RETURN ANY ONE OF THE MOST FREQUENT CHARACTERS
    return most_frequent_chars[0]





