class City:
    city_list = ['Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia']

    def __init__(self, city_code):
        self.selected_city = City.city_list[city_code-1]

    @staticmethod
    def choose_city_code():
        # start to select the city
        # city_code represent the index used to access to the desired city in the class City
        City.print_cities()
        city_code = input('\nSelect the desired city.\t')
        # loop used to check the validity of the current city_code
        while True:
            # city_code conversion to int type
            try:
                if 1 <= int(city_code) <= len(City.city_list):
                    return int(city_code)
                else:
                    city_code = input(f'Invalid number! Must choose from 1 to {len(City.city_list)}.\t')
            # exception occurred selecting a non numerical value
            except ValueError:
                city_code = input(f'Invalid choice! Choose number from 1 to {len(City.city_list)}.\t')

    @staticmethod
    def print_cities():
        for index in range(len(City.city_list)):
            print('{:<3} : {}'.format(index+1, City.city_list[index]))
