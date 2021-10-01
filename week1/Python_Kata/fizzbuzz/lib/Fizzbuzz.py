class Fizzbuzz(object):
    def Solution(self, number):
        """
        :type number: int
        :rtype: List[str]
        """
        if number % 3 == 0 and number % 5 == 0:
            return("FizzBuzz")
        elif number % 3 == 0:
            return("Fizz")
        elif number % 5 == 0:
            return("Buzz")
        elif number == 1:
            return("1")
        elif number == 2:
            return("2")
        else:
            return(str(number))
