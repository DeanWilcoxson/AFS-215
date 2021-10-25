function Solution(number) {
    if ((number % 3 === 0) && (number % 5 === 0)) {
        console.log(number)
        return ("FizzBuzz")
    } else if (number % 3 === 0) {
        console.log(`Fizz, ${number}`)
        return ("Fizz")
    } else if (number % 5 === 0) {
        console.log(`Buzz, ${number}`)
        return ("Buzz")
    } else if (number === 1) {
        console.log(number)
        return ("1")
    } else if (number === 2) {
        console.log(number)
        return ("2")
    } else {
        console.log(`${number} is not divisible by 3 or 5 or equal to 1 or 2.`)
        return (`${number} is not divisible by 3 or 5 or equal to 1 or 2.`)
    }
}
module.exports = Solution