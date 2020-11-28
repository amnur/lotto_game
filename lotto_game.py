import argparse
from lotto.lotto import Lotto
from lotto.extraction import Extraction


def main():
    # let the user choose n° of tickets to generate when he launch the program with argparse argument -n
    first_tickets = True

    while True:
        parser = argparse.ArgumentParser(description='lotto game')
        parser.add_argument('-n', type=int, help='number of tickets')
        args = parser.parse_args()

        # amount of tickets the user wants to generate
        tickets_quantity = args.n
        # maximum amount of tickets the user can generate
        max_tickets = 5
        print('\n\n{::^50}'.format(' WELCOME TO THE ITALIAN LOTTO GAME '))
        # check if the user has choose correctly the amount of tickets to generate
        if tickets_quantity is None or tickets_quantity < 0 or tickets_quantity > max_tickets or not first_tickets:
            tickets_quantity = input(f'\nSelect amount of tickets to generate(max {max_tickets}).\nPress 0 to quit.\t')
            # loop is executed until user inserts valid amount of tickets to generate
            while True:
                try:
                    if int(tickets_quantity) == 0:
                        print('\n\tBye Bye...')
                        quit()
                    elif 1 <= int(tickets_quantity) <= max_tickets:
                        tickets_quantity = int(tickets_quantity)
                        break
                    else:
                        tickets_quantity = input('Invalid selection! Retry\nselected: ')
                # exception occurred in case the user insert literal value
                except ValueError:
                    tickets_quantity = input(f'Invalid choice! Choose n° from 1 to {max_tickets}. Press 0 to quit.\t')

        # tickets_generator return a list of Ticket objects
        lotto = Lotto(tickets_quantity)

        print('{::^50}'.format('  HERE ARE YOUR TICKETS  '))

        for ticket in lotto.tickets:
            ticket.print_ticket()

        input('\nPress any key to see the extraction.\t')

        extraction = Extraction()
        extraction.print_extracted()

        input('\nPress any key to see winner tickets.\t')

        # print winner tickets
        extraction.results(lotto.tickets)

        other_tickets = input('\nPress 0 to quit or press any other key to generate new tickets.\t')
        first_tickets = quit() if other_tickets == '0' else False


if __name__ == '__main__':
    main()
