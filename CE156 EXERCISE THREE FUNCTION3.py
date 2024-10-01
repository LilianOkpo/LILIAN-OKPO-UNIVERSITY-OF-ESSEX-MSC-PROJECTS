#DEFINE THE FUNCTION THAT TAKES A STRING AS AN ARGUMENT
def fun2(input_string):
    letter_count = 0
    space_count = 0
    digit_count = 0

    #COUNT THE NUMBER OF LETTERS, SPACES AND DIGITS IN THE STRING
    for char in input_string:
        if char.isalpha():
            letter_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    #RETURN A TUPLE CONTAINING THE THREE COUNTS
    return letter_count, space_count, digit_count


