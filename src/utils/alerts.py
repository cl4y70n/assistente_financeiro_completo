def check_alerts(df):
    alerts = []
    high_expenses = df[df['Tipo'] == 'Despesa']
    if not high_expenses.empty:
        max_expense = high_expenses['Valor'].max()
        if max_expense > 1000:
            alerts.append(f"Despesa alta detectada: R${max_expense:.2f}")
    return alerts
