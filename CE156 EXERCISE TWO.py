#DEFINE A FUNCTION THAT CHECKS IF THE GIVEN NUMBERS ARE PRIME NUMBERS
def prime_numbers(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
#DEFINE A FUNCTION THAT GETS A LIST OF THE PRIME NUMBERS BETWEEN TWO ARGUMENTS OF POSITIVE INTEGERS
def get_number_primes_between(num1, num2):
    start = min(num1, num2)
    end = max(num1, num2)
    primes = [num for num in range(start, end + 1) if prime_numbers(num)]
    return primes
#CALL THE FUNCTION AND PRINT THE NUMBERS IN THE RETURNED LIST WITH 10 NUMBERS PER OUTPUT LINE
def print_number_primes(primes):
    count = 0
    for prime in primes:
        print(prime, end=' ')
        count += 1
        if count % 10 == 0:
            print()
#DEFINE A PROGRAM THAT ASKS THE USER TO SUPPLY TWO POSITIVE INTEGERS
#AND CHECK THAT THE INPUT IS VALID
def valid_input():
    while True:
        try:
            num1 = int(input("Enter The First Positive Integer: "))
            num2 = int(input("Enter The Second Positive Integer: "))
            if num1 > 0 and num2 > 0:
                return num1, num2
            else:
                print("Please Enter Positive Integers.")
        #PRINT ERROR MESSAGE IF THE USER ENTERS NEGATIVE NUMBERS OR NON NUMERIC INPUTS
        except ValueError:
            print("Invalid Input. Please Enter Valid Positive Integers.")

def main():
    num1, num2 = valid_input()
    primes = get_number_primes_between(num1, num2)
    print("\nPrime Numbers Between", num1, "And", num2, "Are:")
    print_number_primes(primes)

if __name__ == "__main__":
    main()
