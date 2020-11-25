from lotto.city import City
from lotto.numbers import Numbers

class Extraction:
    def __init__(self):
        self.table = {}
        self.generate_extraction()


    def generate_extraction(self):
        numbers_to_extract = 5
        for city in City.city_list:
            self.table[City] = Numbers(numbers_to_extract)



