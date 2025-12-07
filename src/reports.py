class ReportsController:
    def displaySummaryCards(self):
        return{
            "displayCards": [
                {"name": "Monatliche Ausgaben", "amount": 225, "backgroundColor": "from-blue-500 to-blue-600"},
                {"name": "Gesamt-Fonds", "amount": 50, "backgroundColor": "from-purple-500 to-purple-600"},
                {"name": "Durchschnitt", "amount": 75, "backgroundColor": "from-green-500 to-green-600"}
            ],
            "displayButton": [
                {"name": "Export", "color": "border-gray-300 hover:bg-gray-50"},
                 {"name": "Analyse", "color": "bg-blue-600 hover:bg-blue-700 text-white"}
            ]
        }