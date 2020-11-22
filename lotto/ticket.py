from lotto.city import City
from lotto.bet import Bet
import random


class Ticket:
    def __init__(self, city_code, bet_type_code, quantity_to_generate):
        self.city = City(city_code)
        self.bet_type = Bet(bet_type_code)
        self.generated_numbers = []
        self.numbers_generator(quantity_to_generate)

    def numbers_generator(self, quantity_to_generate):
        while len(self.generated_numbers) < quantity_to_generate:
            new_number = random.randint(1, 90)
            if new_number not in self.generated_numbers:
                self.generated_numbers.append(str(new_number))

    def print_ticket(self):
        table_line = '+'+'-'*48+'+'
        print(table_line)
        print('|{:^48}|'.format('TICKET'))
        print(table_line)
        print('|{:^48}|'.format('City: ' + self.city.selected_city.upper()))
        print('|{:^48}|'.format('Bet type: ' + self.bet_type.selected_bet_type.upper()))
        print('|{:^48}|'.format(' '.join(self.generated_numbers)))
        print(table_line)
