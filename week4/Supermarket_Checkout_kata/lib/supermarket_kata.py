class Checkout(object):
    #declaring the array for the items to sit in.
    listItems = []
    #all three (AddItem, AddItemPrice, and AddDiscountRule) in one function.
    #Passing the arguments for the item, declaring a default value of "None" for "Price" and "Discount" they are not required, "Name" is.
    #self refers to "this" class ("Checkout" in this file).
    def Can_Add_Item_andPrice_andDiscount(self, name, price = None, discount = None):
        #declaring a boolean to check whether or not the item is a new item or if it exists in the array
        new = True
        #Declaring the id of each item.
        index = None
        #loop through the length of the array and give each item an id if it is not a new item.
        for i in range(len(self.listItems)):
            print(i)
            if(self.listItems[i]["name"] == name):
                new = False
                index = i
        #if the item is new, give it all the structure the object like this, with these corresponding values, and append it to the array.
        if(new == True):
            item_Obj = {"name": name, "price": price, "discount": discount}
            self.listItems.append(item_Obj)
            return(Checkout.listItems)
        #If the item Objects "Price" value does not match "None", Append the new value to the item object, and return it.
        else:
            if(self.listItems[index]["price"] == None and price != None):
                self.listItems[index]["price"] = price
        #If the item objects "Discount" value does not match "None", Append the new value to the Item object, and return it.
            if(self.listItems[index]["discount"] == None and discount != None):
                self.listItems[index]["discount"] = discount
            return Checkout().listItems

    def Can_Calculate_Current_Total(self):
        pass

    def Can_Add_Multiple_Items_And_Get_Current_Total(self):
        pass

    def Can_Apply_Discount_Rules_To_Total(self):
        pass

    def Throw_Error_For_Item_With_No_Price(self):
        pass