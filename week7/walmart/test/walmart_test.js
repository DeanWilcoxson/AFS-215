const checkout = require("../walmart");
const assert = require("chai").assert;

describe("Checkout", () => {
  it("Can create an instance of the Checkout class", () => {
    let cart = new checkout();
    assert.isDefined(cart.items, "[]");
  });
  it("Can add an item", () => {
    let cart = new checkout();
    assert.equal(cart.addItem("a").name, "a");
  });
  it("Can add an item price", () => {
    let cart = new checkout();
    assert.deepEqual(cart.addItemPrice("b", 10), [{ name: "b", price: 10 }]);
  });
  it("Can calculate the current total", () => {
    let cart = new checkout();
    assert.equal(cart.total());
  });
  it("Can add multiple items and get correct total", () => {
    // let cart = new checkout();
    // assert.equal();
  });
  it("Can add discount rules", () => {
    let cart = new checkout();
    assert.deepEqual(cart.addDiscount(5, "b", 10), 5);
  });

  it("Can apply discount rules to the total", () => {
    // let cart = new checkout();
    // assert.equal();
  });

  it("Exception is thrown for item added without a price", () => {
    // let cart = new checkout();
    // assert.equal();
  });
});
