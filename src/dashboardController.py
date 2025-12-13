from src.DatabaseConnection import DatabaseConnection
from src.models.Budget import Budget
from src.models.Category import Category
from src.models.expense import Expense
import logging
class DashboardController :

    def __init__(self):
      self.db = DatabaseConnection()


    def getTotalExpenses(self): 
       total_expense_query = "SELECT sum(amount) as total FROM expenses"
       result = self.db.fetchone(total_expense_query)
       return result["total"]