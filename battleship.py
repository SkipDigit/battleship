#!/usr/bin/python

# #############################################################

class Player:

    def __init__(self, player_name):
        self.player_name = player_name
        self.grid = {}

        self.ship_size = {
            'Carrier': 5,
            'Battleship': 4,
            'Cruiser': 3,
            'Submarine': 3,
            'Destroyer': 2}

    def make_player_grid():

        # This function returns a dictionary containing every possible grid sector
        # Sample of end result

        #
        #		sector = {
        #			'A1': {
        #				'ship_type': 'None',
        #				'been_shot_at': False
        #				},
        #			'A2': {
        #				''ship_type': 'None',
        #				'been_shot_at': False
        #				}
        #		}

        # create our empty dictionary to stuff things into
        sector = {}

        # loop over the first 10 letters of the alphabet

        from string import ascii_lowercase
        i = 0
        for c in ascii_lowercase:

            # count to 10
            for n in range(1, 11):
                # add to our dictionary
                sector.update(
                    {c.upper() + str(n): {
                        'ship_type': 'None',
                        'been_shot_at': False
                    }
                    }
                )

            # print(c.upper() + str(n))

            if i == 10:
                break
            else:
                i = i + 1

        return sector

    def place_ship(player, ship, top_left, orientation):
            pass

