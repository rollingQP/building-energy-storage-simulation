class Market:
    """
    The Market class
    """

    def __init__(self,
                 simulation
                 ):
        self.simulation=simulation
        pass

    def calc_market_price(self,hour):
        #not yet finished
        self.simulation.market_price_profile[hour]

    def reset(self):
        """
        Resetting the `state_of_charge` of the battery to the `initial_state_of_charge`.
        """
        pass
