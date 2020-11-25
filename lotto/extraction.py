from lotto.city import City
from lotto.numbers import Numbers
from lotto.bet import Bet


class Extraction:
    def __init__(self):
        self.table = {}
        self.generate_extraction()

    def generate_extraction(self):
        numbers_to_extract = 5
        for city in City.city_list:
            self.table[city] = Numbers(numbers_to_extract)

    def print_extracted(self):
        extraction_table_line = '+' + '-' * 28 + '+'
        print(extraction_table_line)
        print('|{:^28}|'.format('EXTRACTION'))
        print(extraction_table_line)
        for city in self.table.keys():
            print('|{:10}{:^18}|'.format(city, ' '.join([str(x) for x in self.table[city].generated_numbers])))
        print(extraction_table_line)

    def results(self, ticket):
        win = []
        if ticket.city.selected_city in self.table.keys():
            for number in ticket.generated_numbers.generated_numbers:
                if number in self.table[ticket.city.selected_city].generated_numbers:
                    win.append(number)
        if len(win) > Bet.bet_type_list.index(ticket.bet_type.selected_bet_type):
            ticket.print_ticket()
            print('|{:^48}|'.format('WINNER NUMBERS'))
            print('|{:^48}|'.format((' '.join(str(x) for x in win))))
            print('+{:-^48}+'.format(''))
            print()

