class CoMachine:  # Coffee Vending Machine
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def deduct(self, water, milk, beans, cups, money):
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += money

    def machine_status(self):
        print(f'\nThe coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.beans}'
              f' of coffee beans\n{self.cups} of disposable cups\n${self.money} of money')

    def coffee_choice(self):
        while True:
            self.buy = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ')
            if self.buy == 'back':
                break
            elif self.buy == '1':  # espresso
                if all([self.water // 250, self.beans // 16]) and self.cups > 0:
                    coffeeMachine.deduct(250, 0, 16, 1, 4)
                    print('I have enough resources, making you a coffee!')
                else:
                    availability = [self.water // 250, self.milk // 1, self.beans // 16, self.cups]
                    print(f'Sorry, not enough {ingredients[availability.index(min(availability))]}!')
            elif self.buy == '2':  # latte
                if all([self.water // 350, self.milk // 75, self.beans // 20]) and self.cups > 0:
                    coffeeMachine.deduct(350, 75, 20, 1, 7)
                    print('I have enough resources, making you a coffee!')
                else:
                    availability = [self.water // 350, self.milk // 75, self.beans // 20, self.cups]
                    print(f'Sorry, not enough {ingredients[availability.index(min(availability))]}!')
            elif self.buy == '3':  # cappuccino
                if all([self.water // 200, self.milk // 100, self.beans // 12]) and self.cups > 0:
                    coffeeMachine.deduct(200, 100, 12, 1, 6)
                    print('I have enough resources, making you a coffee!')
                else:
                    availability = [self.water // 200, self.milk // 100, self.beans // 12, self.cups]
                    print(f'Sorry, not enough {ingredients[availability.index(min(availability))]}!')

    def fill(self):
        self.water += int(input('\nWrite how many ml of water do you want to add:\n> '))
        self.milk += int(input('Write how many ml of milk do you want to add:\n> '))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:\n> '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:\n> '))

    def take(self):
        print(f'I gave you ${abs(self.money)}')
        self.money -= self.money


ingredients = ['water', 'milk', 'coffee beans', 'disposable cups']
coffeeMachine = CoMachine()

while True:
    action = input('\nWrite action (buy, fill, take, remaining, exit):\n> ')
    if action == 'buy':
        coffeeMachine.coffee_choice()
    elif action == 'fill':
        coffeeMachine.fill()
    elif action == 'take':
        coffeeMachine.take()
    elif action == 'remaining':
        coffeeMachine.machine_status()
    elif action == 'exit':
        break
