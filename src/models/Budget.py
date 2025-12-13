class Budget:
    def __init__(self, id,  amount):
        self.id = id
        self.__amount = amount

    def get_amount(self):
        return self.__amount    