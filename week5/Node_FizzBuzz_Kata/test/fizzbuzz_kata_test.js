const assert = require('chai').assert;
const fizzbuzz = require('../fizzbuzz_kata');

describe('FizzBuzz', ()=>{
    it('should return FizzBuzz', () => {
        assert.equal(fizzbuzz(15), 'FizzBuzz')
    });

    it('should return 1', () => {
        assert.equal(fizzbuzz(1), 1)
    });

    it('should return 2', () => {
        assert.equal(fizzbuzz(2), 2)
    });
})