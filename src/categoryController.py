"""
Manages expense categories (zB: Transport, Gesundheit).
"""

from src.DatabaseConnection import DatabaseConnection
from src.models.Category import Category

class CategoryController:
    """Handles category database operations."""

    def __init__(self):
      self.db = DatabaseConnection()
      
    def getCategories(self):
        """
        Gets all categories sorted alphabetically.
        Returns dict with 'categories' key containing list of Category objects.
        """
        rows = self.db.fetchall("SELECT id, name, color, max_amount FROM categories ORDER by name")       
        categories = []

        # Convert database rows to Category objects
        for item in rows:
            category = Category(item["id"], item["name"], item["color"], item["max_amount"])
            categories.append(category)
        return {"categories": categories}
        
    
    def getCategoryByName(self, name):
        """
        Gets a single category by its name.
        Returns None if category doesn't exist.
        """

        row = self.db.fetchone("SELECT id, name, color, max_amount FROM categories WHERE name = ?", (name,)) 
        if row:
            return Category(row["id"], row["name"], row["color"], row["max_amount"])
        return None
    
    def updateCategory(self, name, max_amount):
        """Updates a category"""
        
        update_statement = 'UPDATE categories SET max_amount=? WHERE name = ?'
        self.db.execute(update_statement, (max_amount, name,))
        self.db.commit()
        return True
        
      
