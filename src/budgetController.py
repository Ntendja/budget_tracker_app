from src.DatabaseConnection import DatabaseConnection
from src.models.Budget import Budget

class BudgetController:
    def __init__(self):
      self.db = DatabaseConnection()
      
    def getBudget(self):
        row = self.db.fetchone("SELECT id, amount FROM budget")       
        if row:
                return Budget(row["id"], row["amount"])
        return None
        
    def createOrUpdateBudget(self, amount):
        budget = self.getBudget()
        if budget == None :
           create_query = "INSERT INTO budget (amount) VALUES (?);"
           self.db.execute(create_query, (amount,))
           self.db.commit()
        else:
          update_query = "UPDATE budget SET amount = ? WHERE id = ?"  
          self.db.execute(update_query, (amount, budget.id,))
          self.db.commit()   
        return True
        