import random
import pandas as pd

incomes = []
expenses = []
savings = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


for i in range(12):
    income = random.randint(10000, 100000)
    expense = income * 0.7
    save = income - expense

    incomes.append(income)
    expenses.append(expense)
    savings.append(save)

df = pd.DataFrame({
    "month": months,
    "monthly_income": incomes,
    "monthly_expenses": expenses,
    "monthly_savings": savings
})


df.to_csv("personal_finance_data.csv", index=False)

