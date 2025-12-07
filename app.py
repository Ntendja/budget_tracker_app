from flask import Flask, render_template, request, redirect, url_for
from src.dashboard import DashboardController 
from src.reports import ReportsController
from src.category import CategoryController

app = Flask(__name__)
expenses = []
budget = 0

@app.route('/')
def home():
    dashboard_data = DashboardController()
    dummy_data = dashboard_data.dummyData()
    return render_template('dashboard.html', data=dummy_data)

@app.route('/expense', methods=['GET', 'POST'])
def expense():
    if request.method == 'POST':
       name = request.form.get("name")
       date = request.form.get("date")
       amount = request.form.get("amount")
       category = request.form.get("category")
       description = request.form.get("description")

       new_expense = {
           'name': name,
           'date': date,
           'amount': amount,
           'category': category,
           'description': description
       }

       expenses.append(new_expense)
    return render_template('expense.html', expenses=expenses)

@app.route('/reports')
def reports():
    report_data = ReportsController()
    card_data = report_data.displaySummaryCards()
    return render_template('reports.html', data=card_data)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    create_category = CategoryController() 
    categories = create_category.getCategories()

    if request.method == 'POST':
        monthly_budget = request.form.get('monthly_budget')
        budget.append(monthly_budget)
    return render_template('settings.html', budget=budget, data=categories)

@app.route('/settings/category')
def editCategory():
    return render_template('category.html')

if __name__ == '__main__':
    app.run(debug=True)
