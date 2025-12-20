class Budget:
    """Budget model with getter and setter for amount."""
    
    def __init__(self, id, amount):
        self.id = id
        self.__amount = amount

    def get_amount(self):
        """Returns the budget amount."""
        return self.__amount
    
    def set_amount(self, amount):
        """
        Updates the budget amount.
        
        Args:
            amount (float): New budget amount (must be positive)
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Budget amount must be positive")
        self.__amount = amount
