import yfinance as yf
import streamlit as st
import datetime
yesterday = datetime.datetime.now() - datetime.timedelta(days=2)

st.write("""
# Simple Stock Price App


""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = st.sidebar.selectbox(
    'Select stock Name',
    ('APPLE INC', 'MICROSOFT CORP', 'AMAZON.COM INC','ALPHABET INC','FACEBOOK INC','TENCENT','TESLA INC',
        'GOOGLE INC','CISCO SYSTEMS INC','ORACLE CORP','IBM CORP','CITIGROUP INC','TWITTER INC','CRM CORP',
        'INTEL CORP','IBM CORP',)
)
#get data on this ticker
if tickerSymbol=='APPLE INC':
    tickerSymbol='AAPL'
elif tickerSymbol=='MICROSOFT CORP':
    tickerSymbol='MSFT'
elif tickerSymbol=='AMAZON.COM INC':
    tickerSymbol='AMZN'
elif tickerSymbol=='ALPHABET INC':
    tickerSymbol='AAPL'
elif tickerSymbol=='FACEBOOK INC':
    tickerSymbol='FB'
elif tickerSymbol=='TENCENT':
    tickerSymbol='TCEHY'
elif tickerSymbol=='TESLA INC':
    tickerSymbol='TSLA'
elif tickerSymbol=='GOOGLE INC':
    tickerSymbol='GOOG'
elif tickerSymbol=='CISCO SYSTEMS INC':
    tickerSymbol='CSCO'
elif tickerSymbol=='ORACLE CORP':
    tickerSymbol='ORCL'
elif tickerSymbol=='IBM CORP':
    tickerSymbol='IBM'
elif tickerSymbol=='CITIGROUP INC':
    tickerSymbol='C'
elif tickerSymbol=='TWITTER INC':
    tickerSymbol='TWTR'
elif tickerSymbol=='CRM CORP':
    tickerSymbol='CRM'
elif tickerSymbol=='INTEL CORP':
    tickerSymbol='INTC'

tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker

tickerDf = tickerData.history(period='1d', start='2010-5-31', end=yesterday)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
#f"## {dataset_name} Dataset"
st.write(f"Shown are the stock closing price and volume of  {tickerSymbol} !")
st.write(f"Data Upto   {yesterday} →")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.bar_chart(tickerDf.Close)
try:
    st.image(tickerDf.Close.plot(secondary_y=True).get_figure(), width=500)
except TypeError:
    st.write("Unable to plot")
try:
    st.altair_chart(tickerDf.Close,use_container_width=True)
except TypeError:
    pass
st.write(f" Follow me 👉 https://www.linkedin.com/in/ranjit-maity-75204a131/")
st.write(f" Follow me 👉 https://github.com/RanjitM007 ")
