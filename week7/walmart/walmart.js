class Checkout {
  constructor() {
    this.items = [];
    this.discounts = [];
  }
  addItem = (name) => {
    let check = true;
    for (var i = 0; i < this.items.length; i++) {
      if (this.items[i].name == name) {
        check = false;
        errMsg = "Item already Exists";
        throw Error(errMsg);
      }
    }
    if (check) {
      this.items.push({ name: name });
      return this.items[this.items.length - 1];
    }
  };
  addItemPrice = (name, price) => {
    this.addItem(name);
    for (var i = 0; i < this.items.length; i++) {
      if (this.items[i].name == name) {
        this.items[i] = { name: name, price: price };
        return this.items;
      } else {
        errMsg = "No Item Price";
        throw Error(errMsg);
      }
    }
  };
  addDiscount = (discount, name, price) => {
    this.addItem(name);
    for (var i = 0; i < this.items.length; i++) {
      if (this.items[i].name == name) {
        this.items[i] = { name: name, price: price - discount };
      } else {
        errMsg = "No Item Price";
        throw Error(errMsg);
      }
    }
    return this.items[0].price;
  };
  total = () => {
    let total = 0;
    this.items.map((price) => {
      total += price;
      return total;
    });
  };
  addMultipleItems = ()=>{
      
  }
}
module.exports = Checkout;
