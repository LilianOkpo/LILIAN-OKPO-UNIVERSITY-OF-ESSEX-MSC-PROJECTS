#DEFINE THE PALINDROME FUNCTION
def fun1(s):
    #FOR CASE INSENSITIVITY CONVERT THE STRING TO LOWERCASE
    s = s.lower()
    #TO REMOVE SPACES FROM THE STRING
    s_space = ''.join(s.split())
    #TO CHECK IF THE STRING AND THE REVERSE ARE EQUAL TO THE SAME
    return s == s_space[::-1]



