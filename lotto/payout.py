from lotto.bet import Bet

class Payout:
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

    @staticmethod
    def max_wager_allowed(city_code, bet_type_code, number_quantity):
        max_payout_allowed = 6000000
        max_bet_allowed = 200
        if city_code != 11:
            potential_max_bet = max_payout_allowed//Payout.potential_payout[number_quantity][bet_type_code-1]
            max_bet_allowed = potential_max_bet if potential_max_bet <= max_bet_allowed else max_bet_allowed
            return max_bet_allowed

    @staticmethod
    def calculate_payout(ticket):
        if ticket.city.selected_city.lower() != 'tutte':
            key = len(ticket.generated_numbers.generated_numbers)
            value = Bet.bet_type_list.index(ticket.bet_type.selected_bet_type)
            return float(ticket.amount_wagered * Payout.potential_payout[key][value])
