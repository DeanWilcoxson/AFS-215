## = Steps for Completion
# Explanation
def perfectNumberChecker():
    ## 1. Take in an integer and store it in a variable.
    # The User must enter the number and store it in a variable.
    number = int(input("Please enter a number to check its status: "))
    ## 2. Initialize a variable to count the sum of the proper divisors to 0.
    zeroSum = 0
    ## 3. Use a for loop and an if statement to add the proper divisors of the integer to the sum variable.
    # Use a for loop to generate numbers from 1 to {number} (where {number} is not included as we need the sum of the proper divisors of the number).
    for x in range(1, number):
        # Using an if statement check if the number divided by {x} gives the remainder as 0 which is basically the proper divisor of the integer.
        if(number % x == 0):
            # Then the proper divisors of the number are added to the sum variable.
            zeroSum = zeroSum + x
    ## 4. Check if the sum of the proper divisors of the number is equal to the variable.
    #  If the sum of the proper divisors of the number is equal to the original number, the number is a Perfect number.
    if(zeroSum == number):
        ## 5. Print the final result.
        # The final result is printed
        print("Yep!! Perfect Number!")
    else:
        print("Nope, not a perfect number..")
perfectNumberChecker()