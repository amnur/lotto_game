from lotto.ticket import Ticket
from lotto.city import City
from lotto.bet import Bet


# function called from lotto.py after user selecting the quantity of tickets to generate
def tickets_generator(ticket_quantity):
    horizontal_line = '-'*50
    # list of tickets
    tickets = []
    # each tickets[i] is a class Ticket object with parameter city_list[i], bet_type_list[i], number_quantity_list[i]
    city_list = []
    bet_type_list = []
    number_quantity_list = []

    # start selecting city, bet type and quantity of numbers per each ticket
    for i in range(ticket_quantity):
        
        print(horizontal_line)
        print('{:^50}'.format(f'TICKET {i+1}'))
        print(horizontal_line)

        # City static method invocation to start selecting city
        city_code = City.choose_city_code()
        city_list.append(city_code)

        print(horizontal_line)
        # Bet static method invocation to start selecting bet type
        bet_type_code = Bet.choose_bet_type_code()
        bet_type_list.append(bet_type_code)

        # start to select the quantity of numbers
        max_number = 10
        print(horizontal_line)
        print('How many numbers do you want to play?')
        print(f'Must choose from min = {bet_type_code} to max = {max_number}\t\t')
        # number_quantity represent the quantity of numbers that the class Numbers has to generate
        number_quantity = input('\nSelect the desired amount of numbers.\t')
        # loop used to check the validity of the current number_quantity
        while True:
            # number_quantity conversion to int type
            try:
                if int(bet_type_code) <= int(number_quantity) <= max_number:
                    print(horizontal_line)
                    print()
                    break
                else:
                    number_quantity = input(f'Invalid number! Must choose from {bet_type_code} to {max_number}.\t')
            # exception occurred selecting a non numerical value
            except ValueError:
                number_quantity = input(f'Invalid choice! Choose number from {bet_type_code} to {max_number}.\t')
        number_quantity_list.append(int(number_quantity))

    # class Ticket object generation
    for i in range(ticket_quantity):
        ticket = Ticket(city_list[i], bet_type_list[i], number_quantity_list[i])
        tickets.append(ticket)

    return tickets
