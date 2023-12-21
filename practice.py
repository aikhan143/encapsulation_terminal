class Terminal:

    def __init__(self, card_number, pin_code):
        self.card_number = self.__validity_card_number(card_number)
        self.__pin_code = self.__validity_pin_code(pin_code)
        self.money = 0

    def __validity_card_number(self, card_number):
        if not len(str(card_number)) == 16:
            raise Exception('Invalid card number')
        return card_number
    
    def __validity_pin_code(self, pin_code):
        if not len(str(pin_code)) == 4:
            raise Exception('Invalid pin code')
        return pin_code
    
    def put(self, pin_code, money):
        if pin_code == self.__pin_code:
            self.money += money
        else:
            raise Exception('Wrong pin code')

    def get_money(self, pin_code, money):
        if pin_code == self.__pin_code:
            if self.money >= money:
                if money == round(money):
                    self.money -= money
                else:
                    raise Exception('Invalid amount of money')
            else:
                raise Exception('Not enough money to retrieve')
        else:
            raise Exception('Wrong pin code')
    
    
card = Terminal(1234567891234567, 1234)
card.put(1234, 5655)
print(card.money)
card.put(1234, 56789)
print(card.money)
card.get_money(1234, 62440)
print(card.money)
card.get_money(1234, 4)
print(card.money)