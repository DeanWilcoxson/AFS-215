function Solution(number){
    if ((number % 3 === 0) && (number % 5 === 0)){
        console.log("FizzBuzz")
        return ("FizzBuzz")
    }
    else if (number % 3 === 0){
        console.log("Fizz")
        return ("Fizz")
    }
    else if (number % 5 === 0) {
        console.log("Buzz")
        return ("Buzz")
    }
    else if (number === 1){
        console.log("1")
        return ("1")
    }
    else if (number === 2) {
        console.log("2")
        return ("2")
    }
    else {
        console.log(`${number} is not a passing number.`)
        return (`${number} is not a passing number.`)
    }
}
function test_call_fizzBuzz(){
    Solution(15)
}
test_call_fizzBuzz()
function test_get_one() {
    Solution(1)
}
test_get_one()
function test_get_two() {
    Solution(2)
}
test_get_two()