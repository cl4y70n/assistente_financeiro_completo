import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def analyze_finances(df: pd.DataFrame):
    total_income = df[df['Tipo'] == 'Receita']['Valor'].sum()
    total_expense = df[df['Tipo'] == 'Despesa']['Valor'].sum()
    balance = total_income - total_expense

    return {
        "Total de Receitas": total_income,
        "Total de Despesas": total_expense,
        "Saldo": balance
    }

def predict_cashflow(df: pd.DataFrame):
    df = df.sort_values("Data")
    df["Dia"] = np.arange(len(df))
    X = df[["Dia"]]
    y = df["Valor"]
    model = LinearRegression().fit(X, y)
    future_days = np.arange(len(df), len(df) + 30).reshape(-1, 1)
    predictions = model.predict(future_days)
    return predictions
