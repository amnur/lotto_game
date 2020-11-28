from lotto.city import City
from lotto.bet import Bet
from lotto.numbers import Numbers


class Ticket:
    def __init__(self, city_code, bet_type_code, quantity_to_generate):
        self.city = City(city_code)
        self.bet_type = Bet(bet_type_code)
        self.generated_numbers = Numbers(quantity_to_generate)

    def print_ticket(self):
        print()
        table_line = '+'+'-'*48+'+'
        print(table_line)
        print('|{:^48}|'.format('TICKET'))
        print(table_line)
        print('|{:^48}|'.format('City: ' + self.city.selected_city.upper()))
        print('|{:^48}|'.format('Bet type: ' + self.bet_type.selected_bet_type.upper()))
        # transform list elements from integer to string and transform this list to string using join
        print('|{:^48}|'.format(' '.join([str(x) for x in self.generated_numbers.generated_numbers])))
        print(table_line)
