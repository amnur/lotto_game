from lotto.city import City
from lotto.numbers import Numbers


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
            print('|{:10}{:^18}|'.format(city, ' '.join(self.table[city].generated_numbers)))
        print(extraction_table_line)
