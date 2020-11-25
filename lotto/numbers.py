import random


class Numbers:
    def __init__(self, quantity_to_generate):
        self.generated_numbers = []
        self.numbers_generator(quantity_to_generate)

    def numbers_generator(self, quantity_to_generate):
        while len(self.generated_numbers) < quantity_to_generate:
            new_number = random.randint(1, 90)
            if new_number not in self.generated_numbers:
                self.generated_numbers.append(str(new_number))
