class Bet:
    bet_type_list = ['Ambata', 'Ambo', 'Terna', 'Quaterna', 'Cinquina']

    def __init__(self, bet_type_code):
        self.selected_bet_type = Bet.bet_type_list[bet_type_code-1]

    @staticmethod
    def choose_bet_type_code():
        # start to select the bet type
        Bet.print_bet_types()
        # bet_type represent the index used to access to the desired bet type in the class Bet
        bet_type = input('\nSelect the desired bet type.\t')
        # loop used to check the validity of the current bet_type
        while True:
            # bet_type conversion to int type
            try:
                if 1 <= int(bet_type) <= len(Bet.bet_type_list):
                    return int(bet_type)
                else:
                    bet_type = input(f'Invalid number! Must choose from 1 to {len(Bet.bet_type_list)}.\t')
            # exception occurred selecting a non numerical value
            except ValueError:
                bet_type = input(f'Invalid choice! Choose number from 1 to {len(Bet.bet_type_list)}.\t')

    @staticmethod
    def print_bet_types():
        for index in range(len(Bet.bet_type_list)):
            print('{:<3} : {}'.format(index + 1, Bet.bet_type_list[index]))
