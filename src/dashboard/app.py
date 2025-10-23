import streamlit as st
from src.utils.data_loader import load_data
from src.utils.analysis import analyze_finances, predict_cashflow
from src.utils.alerts import check_alerts
import pandas as pd

st.set_page_config(page_title="Assistente Financeiro", layout="wide")

st.title("💰 Assistente Financeiro Inteligente")

uploaded_file = st.file_uploader("Envie sua planilha de despesas e receitas (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Dados carregados")
    st.dataframe(df)

    summary = analyze_finances(df)
    st.subheader("📈 Resumo Financeiro")
    st.write(summary)

    prediction = predict_cashflow(df)
    st.subheader("🔮 Previsão de Fluxo de Caixa")
    st.line_chart(prediction)

    alerts = check_alerts(df)
    if alerts:
        st.warning("⚠️ Alertas detectados:")
        for alert in alerts:
            st.write(f"- {alert}")
