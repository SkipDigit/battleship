
# for use in instantiating, but not anywhere else.
# can't seem to find any other way to make a method available at init
# but private otherwise.

def make_grid():

    # This function should only be called on init of the Player class
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


