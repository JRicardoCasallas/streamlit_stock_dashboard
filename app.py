import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

# 🎯 Título de la app
st.title("📊 Dashboard Comparativo de Acciones")

# 📌 Barra lateral de configuración
st.sidebar.header("Configuración")

# Lista de tickers disponibles
tickers_list = [
    "AMZN", "META", "SPY", "AAPL", "MSFT", "GOOGL", "TSLA", "NVDA", "IBM"
]

# Selector múltiple
tickers = st.sidebar.multiselect(
    "Selecciona los activos:",
    tickers_list,
    default=["AMZN", "META", "SPY"]
)

period = st.sidebar.selectbox("Periodo", ["1mo", "3mo", "6mo", "1y", "2y"], index=2)
interval = st.sidebar.selectbox("Intervalo", ["1d", "1wk", "1mo"], index=0)

if tickers:
    # Descargar datos de varios tickers
    df = yf.download(tickers, period=period, interval=interval)["Close"]

    # Resetear índice para usar en Plotly
    df = df.reset_index()

    # 📊 Gráfico comparativo de líneas
    fig = px.line(
        df,
        x="Date",
        y=df.columns[1:],  # todas las columnas menos Date
        title=f"Evolución comparativa de: {', '.join(tickers)}"
    )
    st.plotly_chart(fig, use_container_width=True)

    # 📌 Mostrar últimos precios
    st.subheader("📌 Últimos precios")
    last_prices = df.tail(1).T
    last_prices.columns = ["Último precio"]
    st.write(last_prices)

    # 📌 Rendimiento porcentual
    st.subheader("📊 Rendimiento en el periodo seleccionado")
    returns = (df.set_index("Date").iloc[-1] / df.set_index("Date").iloc[0] - 1) * 100
    ranking = returns.sort_values(ascending=False).to_frame("Rendimiento (%)")
    st.write(ranking)

    # 📊 Gráfico de barras con el ranking
    st.subheader("📊 Ranking visual de rendimientos (%)")
    fig_bar = px.bar(
        ranking,
        x=ranking.index,
        y="Rendimiento (%)",
        color="Rendimiento (%)",
        color_continuous_scale="Bluered_r",
        title="Ranking de Rendimientos"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # ⭐ Top 3 Ganadores y Perdedores
    st.subheader("🏆 Top 3 Ganadores y Perdedores")

    top_3 = ranking.head(3)
    bottom_3 = ranking.tail(3)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🚀 Top 3 Ganadores")
        st.write(top_3)

    with col2:
        st.markdown("### 🔻 Top 3 Perdedores")
        st.write(bottom_3)

else:
    st.warning("Selecciona al menos un activo en la barra lateral")

