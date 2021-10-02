class Fizzbuzz(object):
    def Solution(self, number):
        """:type number: int
        :rtype: List[str]"""
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            return("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
            return("Fizz")
        elif number % 5 == 0:
            print("Buzz")
            return("Buzz")
        elif number == 1:
            print("1")
            return("1")
        elif number == 2:
            print("2")
            return("2")
        else:
            print(str(number))
            return(str(number))
