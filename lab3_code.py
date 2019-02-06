class Currency:
    unit_name = "currency" # class variable because it's true of ALL instances of this class (unless overridden in a subclass)

    def __init__(self, value):
        self.value = value
        self.base_rate = 1 #always

    def conversion(self, result_currency_reference):
        if(type(self) == Pound):
            rate = Pound.rate
        elif (type(self) == Yuan):
            rate = Yuan.rate
        elif (type(self) == Dollar):
            rate = Dollar.rate
        else:
            return "Can't convert. Please enter a valid currency."

        #Conversion
        value_in_currency = self.value * rate
        value_at_reference_rate = value_in_currency / result_currency_reference.rate
        return result_currency_reference(value_at_reference_rate)


class Dollar(Currency):
    unit_name = "Dollar"
    rate = 20

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return "{} {}".format(self.value,"Dollar" + "s" * (self.value > 1))

class Yuan(Currency):
    unit_name = "Yuan"
    rate = 8

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return "{} {}".format(self.value,"Yuan")

class Pound(Currency):
    unit_name = "Pound"
    rate = 15

    def __init__(self, value):
        super().__init__(value)
    def __str__(self):
        return "{} {}".format(self.value,"Pound" + "s" * (self.value > 1))

### PROVIDED CODE you can try:
# dollar = Dollar(1)
# pound = Pound(1)
# yuan = Yuan(1)
#
# print(yuan.conversion(Pound))
# # 0.5333333333333333 Pound
#
# print(pound.conversion(Pound))
# # 1.0 Pound
#
# print(pound.conversion(Dollar))
# # 0.75 Dollar
#
# print(dollar)
# # 1 Dollar
#
# two_dollars = Dollar(2)
# print(two_dollars)
# # 2 Dollars


class Bank:
   def __init__(self, name, unit, initial_value=0):
       self.name = name
       self.unit = unit
       self.current_account = unit(initial_value)

   def __str__(self):
       return "{} Bank holds the {} currency and currently holds {} of {}".format(self.name, self.unit, self.current_account, self.unit)

   def deposit(self, inst):
       if not self.unit == type(inst):
           return "ERROR: cannot deposit that currency."
       else:
           self.current_account.value += inst.value
           return "successful deposit"


# jpMorgan = Bank("J.P.Morgan", Dollar, 1)
# barclays = Bank("Barclays", Pound, 1)
# bank_of_china = Bank("Bank of China", Yuan, 1)
#
#
# print(jpMorgan.current_account.value)
# # 1
#
# dollar = Dollar(1)
# print(jpMorgan.deposit(dollar))
# # should show: 'successful deposit'
#
# print(jpMorgan.current_account.value)
# # should show: 2
#
# print(jpMorgan.deposit(pound))
# # should show: 'ERROR: cannot deposit that currency.'
