const assert = require("chai").assert;
const fizzbuzz = require("../FizzBuzz");

describe("FizzBuzz", () => {
  it("should return FizzBuzz", () => {
    assert.equal(fizzbuzz(15), "FizzBuzz");
  });
  it("should return 1", () => {
    assert.equal(fizzbuzz(1), 1);
  });
  it("should return 2", () => {
    assert.equal(fizzbuzz(2), 2);
  });
  it("should return Fizz", () => {
    assert.equal(fizzbuzz(3), "Fizz");
  });
  it("should return Buzz", () => {
    assert.equal(fizzbuzz(5), "Buzz");
  });
  it("should return Fizz", () => {
    assert.equal(fizzbuzz(6), "Fizz");
  });
  it("should return Buzz", () => {
    assert.equal(fizzbuzz(10), "Buzz");
  });
  it("should return FizzBuzz", () => {
    assert.equal(fizzbuzz(15), "FizzBuzz");
  });
});
