import argparse
from lotto.lotto import Lotto
from lotto.extraction import Extraction


def main():
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
        if tickets_quantity is None or tickets_quantity < 0 or tickets_quantity > max_tickets:
            tickets_quantity = input(f'\nSelect the amount of tickets to generate(max {max_tickets}).\nPress 0 to quit.\t')
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
                    tickets_quantity = input('Invalid choice! Choose number from 1 to %s. Press 0 to quit.\t' % max_tickets)

        # tickets_generator return a list of Ticket objects
        lotto = Lotto(tickets_quantity)

        for ticket in lotto.tickets:
            ticket.print_ticket()

        see_extraction = input('Press any key to see the extraction.\t')

        extacted = Extraction()
        extacted.print_extracted()

        other_tickets = input('Press 0 to quit or press any other key to generate new tickets.\t')
        if other_tickets == '0':
            quit()


if __name__ == '__main__':
    main()
