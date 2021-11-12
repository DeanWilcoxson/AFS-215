class Checkout {
  constructor() {
    this.items = [];
  }
  canAddItem = (name) => {
    let check = true;
    for (var i = 0; i < this.items.length; i++) {
      if (this.items[i].name == name) {
        check = false;
        let errMsg = "Item already Exists";
        return errMsg;
      }
    }
    if (check) {
      this.items.push({ name: name });
      return this.items[this.items.length - 1];
    }
  };
  canAddItemPrice = (name, price) => {
    this.canAddItem(name);
    for (var i = 0; i < this.items.length; i++) {
      if (this.items[i].name == name) {
        this.items[i].price = price;
        return this.items;
      }
    }
  };
  canCalculateCurrentTotal = () => {
    let total = 0;
    for (var i = 0; i < this.items.length; i++) {
      var item = this.items[i];
      if (!item.price) {
        let errMsg = "No Item Price";
        return errMsg;
      } else {
        total += item.price;
      }
    }
    return total;
  };
  canAddMultipleItemsAndGetCorrectTotal = (name, price) => {
    let total = 0;
    this.canAddItemPrice(name, price);
    this.canAddItemPrice(name, price);
    this.items.map((price) => {
      total += price;
      return total;
    });
  };
  canAddDiscountRule = (discount, name, price) => {
    this.canAddItem(name);
    for (var i = 0; i < this.items.length; i++) {
      if (this.items[i].name == name) {
        this.items[i] = { name: name, price: price - discount };
      }
    }
    return this.items[0].price;
  };
}
module.exports = Checkout;
