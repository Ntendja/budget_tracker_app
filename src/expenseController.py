from src.DatabaseConnection import DatabaseConnection
from src.models.expense import Expense
import logging

"""
Manages all expense-related database operations.
"""


class ExpenseController:
    """Handles CRUD operations and queries for expenses."""

    def __init__(self):
      self.db = DatabaseConnection()
      
    def addExpenses(self, name, date, amount, category, description):
        """ Creates a new expense """

        insert_param="INSERT into expenses (name, date, amount, category, description ) values(?,?,?,?,?);"
        self.db.execute(insert_param, (name,date, amount, category, description,))
        self.db.commit()
        return True
    
    def getExpenses(self):
        """ Retrieves all expenses from the database """

        query = "SELECT id, name, date, amount, category, description FROM expenses"
        rows = self.db.fetchall(query)
        expenses = []
        for row in rows:
            expense = Expense(row["id"], row["name"], row["date"], row["amount"], row["category"], row["description"])
            logging.warning(expense.get_name())
            expenses.append(expense)
        return expenses

    def getExpenseByCategory(self):
        """ Groups expenses by category and calculates totals """

        query = "SELECT category, sum(amount) as amount,  color FROM expenses join categories on categories.name == category group by category"
        rows = self.db.fetchall(query)
        return rows


    def getExpense(self, id):
       """ Retrieves a single expense by ID """

       query = "SELECT * FROM expenses WHERE id = ?"
       row = self.db.fetchone(query, (id,))
       if row:
            return Expense(row["id"], row["name"], row["date"], row["amount"], row["category"], row["description"])
       return None 
    
    def updateExpense(self, id, name, date, amount, category, description):
        """ Updates an existing expense """
        update_statement = 'UPDATE expenses SET name=?, date=?, amount=?, category=?, description=? WHERE id = ?'
        self.db.execute(update_statement, (name, date, amount, category, description, id,))
        self.db.commit()
        return True
      
    def deleteExpense(self, id):
        """ Deletes an expense by ID """
        query = "DELETE FROM expenses WHERE id = ?" 
        self.db.execute(query, (id,))   
        self.db.commit()
        return True