"""
Provides summary data for the dashboard view.
"""

from src.DatabaseConnection import DatabaseConnection
class DashboardController :
    """Handles dashboard statistics and aggregated data."""

    def __init__(self):
      self.db = DatabaseConnection()


    def getTotalExpenses(self):
       """
        Calculates the sum of all expenses.
        Returns 0 if no expenses exist.
        """ 
       total_expense_query = "SELECT sum(amount) as total FROM expenses"
       result = self.db.fetchone(total_expense_query)
       return result["total"]