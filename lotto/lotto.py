from lotto.ticket import Ticket
from lotto.city import City
from lotto.bet import Bet


# this class generates the amount of Ticket objects required from the user
class Lotto:

    def __init__(self, ticket_quantity):
        self.tickets = []
        self.generates_tickets(ticket_quantity)

    def generates_tickets(self, ticket_quantity):
        horizontal_line = '-'*50

        # start selecting city, bet type and quantity of numbers per each ticket
        for i in range(ticket_quantity):

            print(horizontal_line)
            print('{:^50}'.format(f'TICKET {i+1}'))
            print(horizontal_line)

            # CITY SELECTION
            # City static method invocation to start selecting city
            city_code = City.choose_city_code()

            print(horizontal_line)

            # BET TYPE SELECTION
            # Bet static method invocation to start selecting bet type
            bet_type_code = Bet.choose_bet_type_code()

            # QUANTITY OF NUMBER SELECTION
            max_number = 10
            print(horizontal_line)
            print('How many numbers do you want to play?')
            print(f'Must choose from min = {bet_type_code} to max = {max_number}\t\t')
            # number_quantity represent the quantity of numbers to generate for each ticket
            number_quantity = input('\nSelect the desired amount of numbers.\t')
            # loop used to check the validity of the current number_quantity
            while True:
                # number_quantity conversion to int type
                try:
                    if int(bet_type_code) <= int(number_quantity) <= max_number:
                        number_quantity = int(number_quantity)
                        print(horizontal_line)
                        print()
                        break
                    else:
                        number_quantity = input(f'Invalid number! Must choose from {bet_type_code} to {max_number}.\t')
                # exception occurred selecting a non numerical value
                except ValueError:
                    number_quantity = input(f'Invalid choice! Choose number from {bet_type_code} to {max_number}.\t')

            # CREATE A TICKET OBJECT AND INSERT IT IN THE LIST
            self.tickets.append(Ticket(city_code, bet_type_code, number_quantity))
