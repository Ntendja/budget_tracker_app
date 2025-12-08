class DashboardController :
    def dummyData(self, budget, expenses):
        return {
            "totalExpenses" : 625,
            "monthBudget" : budget,
            "remainingBudget" : 200,
            "expenses": expenses,
            "categoriesExpenses": [
                {"name": "Lebensmittel", "amount": "150", "color":"bg-blue-600", "percentage" : 30},
                {"name": "Transport", "amount": "80", "color":"bg-green-600", "percentage" : 50},
                {"name": "Unterhaltung", "amount": "200", "color":"bg-purple-600", "percentage" : 90}
            ]
        }