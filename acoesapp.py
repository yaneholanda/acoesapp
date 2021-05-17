import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Aplicativo simples para consulta de Ações

Abaixo, você encontra os valores de **fechamento** e de ***volume*** do Google!

""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = 'id', start ='2010-5-31', end ='2021-5-31')


st.write("""
# Valor de Fechamento
""")
st.line_chart(tickerDf.Close)

st.write("""
# Volume
""")
st.line_chart(tickerDf.Volume)
