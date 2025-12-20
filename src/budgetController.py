"""
Manages the global monthly budget.
"""

from src.DatabaseConnection import DatabaseConnection
from src.models.Budget import Budget

class BudgetController:
    """Handles budget database operations."""
    def __init__(self):
      self.db = DatabaseConnection()
      
    def getBudget(self):
        """
        Gets the current budget from database.
        Returns None if no budget exists.
        """
        row = self.db.fetchone("SELECT id, amount FROM budget")       
        if row:
                return Budget(row["id"], row["amount"])
        return None
        
    def createOrUpdateBudget(self, amount):
        """
        Creates a new budget or updates existing one.
        Returns True on success.
        """
        budget = self.getBudget()
        if budget == None :
           # Create new budget
           create_query = "INSERT INTO budget (amount) VALUES (?);"
           self.db.execute(create_query, (amount,))
           self.db.commit()
        else:
          # Update existing budget
          update_query = "UPDATE budget SET amount = ? WHERE id = ?"  
          self.db.execute(update_query, (amount, budget.id,))
          self.db.commit()   
        return True