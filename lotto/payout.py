from lotto.bet import Bet


class Payout:
    """
    - keys represents quantity of number generated for each ticket
    - each element of the list represents the potential payout for each bet type with that quantity of number generated
      ['ambata', 'ambo', 'terna', 'quaterna', 'cinquina'].
      If the selected city is 'Tutte' each potential payout must be divided by 10.
    """
    potential_payout = {
        1: [11.23],
        2: [5.62, 250],
        3: [3.74, 83.33, 4500],
        4: [2.81, 41.67, 1125, 120000],
        5: [2.25, 25, 450, 24000, 6000000],
        6: [1.87, 16.67, 225, 8000, 1000000],
        7: [1.60, 11.90, 128.57, 3428.57, 285714.29],
        8: [1.40, 8.93, 80.36, 1714.29, 107142.86],
        9: [1.25, 6.94, 53.57, 952.38, 47619.05],
        10: [1.12, 5.56, 37.50, 571.43, 23809.52]
    }

    """
    max_wager_allowed calculates the max bet allowed in order to avoid the user to win more than the max payout allowed
    which is 6 millions. This value can't be more than 200 €.
    """
    @staticmethod
    def max_wager_allowed(city_code, bet_type_code, number_quantity):
        max_payout_allowed = 6000000
        max_bet_allowed = 200
        potential_max_bet = max_payout_allowed//Payout.potential_payout[number_quantity][bet_type_code-1]
        potential_max_bet = potential_max_bet * 10 if city_code == 11 else potential_max_bet
        max_bet_allowed = potential_max_bet if potential_max_bet <= max_bet_allowed else max_bet_allowed
        return max_bet_allowed

    """
    For each ticket, calculate_payout takes the quantity of number generated and the bet type index and calculates the 
    payout using these values respectively as key and index of the value list inside potential_payout and multiplying 
    the value for the amount wagered. If the selected city is 'Tutte', the payout is divided by 10.
    """
    @staticmethod
    def calculate_payout(ticket):
        key = len(ticket.generated_numbers.generated_numbers)
        value = Bet.bet_type_list.index(ticket.bet_type.selected_bet_type)
        payout = ticket.amount_wagered * Payout.potential_payout[key][value]
        return float(payout) if ticket.city.selected_city.lower() != 'tutte' else float(payout/10)
