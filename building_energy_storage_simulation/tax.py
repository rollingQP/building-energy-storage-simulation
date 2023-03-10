class Tax:
    """
    The Tax class
    """

    def __init__(self,
                 method = "constant",
                 tax_table = [0.03942],
                 ):
        self.method = method
        self.tax_table = tax_table
        
    def calc_tax(self, electricity_draw_from_grid) -> float:
        if self.method == "constant":
            return electricity_draw_from_grid * self.tax_table[0]
        elif self.method == "tiered":
            pass

    def reset(self):
        """
        Resetting the `state_of_charge` of the battery to the `initial_state_of_charge`.
        """
        pass
