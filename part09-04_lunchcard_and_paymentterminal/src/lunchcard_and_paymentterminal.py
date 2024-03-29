class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the
        # price of the lunch, increase the number of lunches sold,
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        price = 2.50
        if payment >= price:
            self.funds += price
            self.lunches += 1
            return payment - price
        else:
            return payment

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the
        # price of the lunch, increase the number of lunches sold,
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        price = 4.30
        if payment >= price:
            self.funds += price
            self.specials += 1
            return payment - price
        else:
            return payment

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the
        # price of the lunch, increase the number of lunches sold,
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        price = 2.50
        if payment >= price:
            self.funds += price
            self.lunches += 1
            return payment - price
        else:
            return payment

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the
        # price of the lunch, increase the number of lunches sold,
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        price = 4.30
        if payment >= price:
            self.funds += price
            self.specials += 1
            return payment - price
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card,
        # subtract the price of the lunch from the balance
        # and return True. If not, return False.
        price = 2.50
        if card.balance >= price:
            card.balance -= price
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card,
        # subtract the price of the lunch from the balance
        # and return True. If not, return False.
        price = 4.30
        if card.balance >= price:
            card.balance -= price
            self.specials += 1
            return True
        else:
            return False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the 
        # price of the lunch, increase the number of lunches sold, 
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        price = 2.50
        if payment >= price:
            self.funds += price
            self.lunches += 1
            return payment - price
        else:
            return payment

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the 
        # price of the lunch, increase the number of lunches sold, 
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        price = 4.30
        if payment >= price:
            self.funds += price
            self.specials += 1
            return payment - price
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, 
        # subtract the price of the lunch from the balance
        # and return True. If not, return False.
        price = 2.50
        if card.balance >= price:
            card.balance -= price
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, 
        # subtract the price of the lunch from the balance
        # and return True. If not, return False.
        price = 4.30
        if card.balance >= price:
            card.balance -= price
            self.specials += 1
            return True
        else:
            return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        # Deposit money onto the LunchCard and add the equivalent amount to the terminal funds
        card.balance += amount
        self.funds += amount

if __name__ == "__main__":
    exactum = PaymentTerminal()

    