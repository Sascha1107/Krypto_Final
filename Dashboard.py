import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

#1. Verbindungsaufbau zur Datenbank
connection = sqlite3.connect("C:/Users/Sascha/Downloads/historical_crypto_data.db")
cur = connection.cursor()


#2. Liste der Tabellennamen ermitteln und daraus den Options-filter erstellen
cur.execute("select name from sqlite_master where type='table';")
t = cur.fetchall()
table_List = []


for i in t:
    table = i[0]
    table_List.append(table)

def wide_space_default():
    st.set_page_config(layout="wide")

wide_space_default()

st.header("Crypto-Dashboard")

option = st.selectbox(
 'Zeitraum',
table_List)

st.write("Auwahl:", option)



#3. Abfragen der Daten je Zeitraum

one_min = cur.execute('select * from crypto_prices_1Min')
five_min = cur.execute('select * from crypto_prices_5m')
fiveteen_min = cur.execute('select * from crypto_prices_15m')
thirty_min = cur.execute('select * from crypto_prices_30m')
sixty_min = cur.execute('select * from crypto_prices_60m')
four_hours = cur.execute('select * from crypto_prices_4h')




#4. Liste der Tabellennamen ermitteln und daraus den Options-filter erstellen

#4.1 crypto_prices_1Mon

SOL_ONE_MONTH = []
BTC_ONE_MONTH = []
ETH_ONE_MONTH = []
Datum_ONE_MONTH = []


one_month= cur.execute('select * from crypto_prices_1Mon')
time_frame = one_month.fetchall()

for i in time_frame:
    if 'BTCUSDT' in i:
        x = i[5]
        y = i[1]
        stripped = y[: 10].strip()
        BTC_ONE_MONTH.append(x)
        Datum_ONE_MONTH.append(stripped)
for i in time_frame:
    if 'SOLUSDT' in i:
        x = i[5]
        SOL_ONE_MONTH.append(x)

for i in time_frame:
    if 'ETHUSDT' in i:
        x = i[5]
        ETH_ONE_MONTH.append(x)

df = pd.DataFrame(list(zip(Datum_ONE_MONTH, BTC_ONE_MONTH, SOL_ONE_MONTH, ETH_ONE_MONTH)),
                      columns=['Datum', 'BITCOIN', 'SOLANA', 'ETHEREUM'])


if option == "crypto_prices_1Mon":
    #st.column_config.Column(width="large")
    col1, col2, col3 = st.columns([1, 1, 1])

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=Datum_ONE_MONTH, y=BTC_ONE_MONTH, name="Bitcoin"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=Datum_ONE_MONTH, y=SOL_ONE_MONTH, name="Solana"),
        secondary_y=True,
    )
    fig.update_layout(
        title_text=f"Kursvergleich - BTC. vs. SOL"
    )
    fig.update_xaxes(title_text="Zeitraum")
    fig.update_yaxes(title_text="Bitcoin", secondary_y=False)
    fig.update_yaxes(title_text="Solana", secondary_y=True)

    df_updated = df[['BITCOIN', 'SOLANA']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)

    with col1:
        st.write(f"Korrelation: {correl_updated}")
        st.plotly_chart(fig)

    fig_two = make_subplots(specs=[[{"secondary_y": True}]])
    fig_two.add_trace(
        go.Scatter(x=Datum_ONE_MONTH, y=BTC_ONE_MONTH, name="Bitcoin"),
        secondary_y=False,
    )
    fig_two.add_trace(
        go.Scatter(x=Datum_ONE_MONTH, y=ETH_ONE_MONTH, name="Ethereum"),
        secondary_y=True,
    )
    fig_two.update_layout(
        title_text=f"Kursvergleich - BTC vs.ETH"
    )
    fig_two.update_xaxes(title_text="Zeitraum")
    fig_two.update_yaxes(title_text="Bitcoin", secondary_y=False)
    fig_two.update_yaxes(title_text="Ethereum", secondary_y=True)

    df_updated = df[['BITCOIN', 'ETHEREUM']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)

    with col2:
        st.write(f"Korrelation: {correl_updated}")
        st.plotly_chart(fig_two)

    fig_three = make_subplots(specs=[[{"secondary_y": True}]])
    fig_three.add_trace(
        go.Scatter(x=Datum_ONE_MONTH, y=SOL_ONE_MONTH, name="Solana"),
        secondary_y=False,
    )
    fig_three.add_trace(
        go.Scatter(x=Datum_ONE_MONTH, y=ETH_ONE_MONTH, name="Ethereum"),
        secondary_y=True,
    )
    fig_three.update_layout(
        title_text=f"Kursvergleich - SOL vs ETH"
    )
    fig_three.update_xaxes(title_text="Zeitraum")
    fig_three.update_yaxes(title_text="Solana", secondary_y=False)
    fig_three.update_yaxes(title_text="Ethereum", secondary_y=True)

    df_updated = df[['ETHEREUM', 'SOLANA']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)

    with col3:
        st.write(f"Korrelation: {correl_updated}")
        st.plotly_chart(fig_three)

#4.2 crypto_prices_1W

SOL_ONE_WEEK = []
BTC_ONE_WEEK = []
ETH_ONE_WEEK = []
Datum_ONE_WEEK = []


one_week= cur.execute('select * from crypto_prices_1W')
time_frame = one_week.fetchall()

for i in time_frame:
    if 'BTCUSDT' in i:
        x = i[5]
        y = i[1]
        stripped = y[: 10].strip()
        BTC_ONE_WEEK.append(x)
        Datum_ONE_WEEK.append(stripped)
for i in time_frame:
    if 'SOLUSDT' in i:
        x = i[5]
        SOL_ONE_WEEK.append(x)

for i in time_frame:
    if 'ETHUSDT' in i:
        x = i[5]
        ETH_ONE_WEEK.append(x)

df_one_week = pd.DataFrame(list(zip(Datum_ONE_WEEK, BTC_ONE_WEEK, SOL_ONE_WEEK, ETH_ONE_WEEK)),
                      columns=['Datum', 'BITCOIN', 'SOLANA', 'ETHEREUM'])


if option == "crypto_prices_1W":
    #st.column_config.Column(width="large")
    col1, col2, col3 = st.columns([1, 1, 1])

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=Datum_ONE_WEEK, y=BTC_ONE_WEEK, name="Bitcoin"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=Datum_ONE_WEEK, y=SOL_ONE_WEEK, name="Solana"),
        secondary_y=True,
    )
    fig.update_layout(
        title_text=f"Kursvergleich - BTC. vs. SOL"
    )
    fig.update_xaxes(title_text="Zeitraum")
    fig.update_yaxes(title_text="Bitcoin", secondary_y=False)
    fig.update_yaxes(title_text="Solana", secondary_y=True)

    df_updated = df[['BITCOIN', 'SOLANA']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)

    with col1:
        st.write(f"Korrelation: {correl_updated}")
        st.plotly_chart(fig)

    fig_two = make_subplots(specs=[[{"secondary_y": True}]])
    fig_two.add_trace(
        go.Scatter(x=Datum_ONE_WEEK, y=BTC_ONE_WEEK, name="Bitcoin"),
        secondary_y=False,
    )
    fig_two.add_trace(
        go.Scatter(x=Datum_ONE_WEEK, y=ETH_ONE_WEEK, name="Ethereum"),
        secondary_y=True,
    )
    fig_two.update_layout(
        title_text=f"Kursvergleich - BTC vs.ETH",
    )
    fig_two.update_xaxes(title_text="Zeitraum")
    fig_two.update_yaxes(title_text="Bitcoin", secondary_y=False)
    fig_two.update_yaxes(title_text="Ethereum", secondary_y=True)

    df_updated = df[['ETHEREUM', 'BITCOIN']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)

    with col2:
        st.write(f"Korrelation: {correl_updated}")
        st.plotly_chart(fig_two)

    fig_three = make_subplots(specs=[[{"secondary_y": True}]])
    fig_three.add_trace(
        go.Scatter(x=Datum_ONE_WEEK, y=SOL_ONE_WEEK, name="Solana"),
        secondary_y=False,
    )
    fig_three.add_trace(
        go.Scatter(x=Datum_ONE_WEEK, y=ETH_ONE_WEEK, name="Ethereum"),
        secondary_y=True,
    )
    fig_three.update_layout(
        title_text=f"Kursvergleich - SOL vs ETH"
    )
    fig_three.update_xaxes(title_text="Zeitraum")
    fig_three.update_yaxes(title_text="Solana", secondary_y=False)
    fig_three.update_yaxes(title_text="Ethereum", secondary_y=True)

    df_updated = df[['ETHEREUM', 'SOLANA']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)

    with col3:
        st.write(f"Korrelation: {correl_updated}")
        st.plotly_chart(fig_three)


#4.3 crypto_prices_1D

SOL_ONE_DAY = []
BTC_ONE_DAY = []
ETH_ONE_DAY = []
Datum_ONE_DAY = []


one_week= cur.execute('select * from crypto_prices_1d')
time_frame = one_week.fetchall()

for i in time_frame:
    if 'BTCUSDT' in i:
        x = i[5]
        y = i[1]
        stripped = y[: 10].strip()
        BTC_ONE_DAY.append(x)
        Datum_ONE_DAY.append(stripped)
for i in time_frame:
    if 'SOLUSDT' in i:
        x = i[5]
        SOL_ONE_DAY.append(x)

for i in time_frame:
    if 'ETHUSDT' in i:
        x = i[5]
        ETH_ONE_DAY.append(x)

df_one_day = pd.DataFrame(list(zip(Datum_ONE_DAY, BTC_ONE_DAY, SOL_ONE_DAY, ETH_ONE_DAY)),
                      columns=['Datum', 'BITCOIN', 'SOLANA', 'ETHEREUM'])


if option == "crypto_prices_1d":
    #st.column_config.Column(width="large")
    col1, col2, col3 = st.columns([1, 1, 1])

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=BTC_ONE_DAY, name="Bitcoin",fillcolor="#fff"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=SOL_ONE_DAY, name="Solana"),
        secondary_y=True,
    )
    fig.update_layout(
        title_text=f"Kursvergleich - BTC. vs. SOL"
    )
    fig.update_xaxes(title_text="Zeitraum")
    fig.update_yaxes(title_text="Bitcoin", secondary_y=False)
    fig.update_yaxes(title_text="Solana", secondary_y=True)

    df_updated = df[['BITCOIN', 'SOLANA']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)
    pre_value = correl_updated * 100
    bar_value = int(pre_value)

    with col1:
        st.markdown(f"#### Korrelation:")
        my_bar = st.progress(0)
        st.markdown(f"# {correl_updated}")
        st.plotly_chart(fig)
        for percent_complete in range(bar_value):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1,)
        time.sleep(1)



    fig_two = make_subplots(specs=[[{"secondary_y": True}]])
    fig_two.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=BTC_ONE_DAY, name="Bitcoin"),
        secondary_y=False,
    )
    fig_two.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=ETH_ONE_DAY, name="Ethereum"),
        secondary_y=True,
    )
    fig_two.update_layout(
        title_text=f"Kursvergleich - BTC vs.ETH"
    )
    fig_two.update_xaxes(title_text="Zeitraum")
    fig_two.update_yaxes(title_text="Bitcoin", secondary_y=False)
    fig_two.update_yaxes(title_text="Ethereum", secondary_y=True)

    df_updated = df[['BITCOIN', 'ETHEREUM']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)
    pre_value = correl_updated * 100
    bar_value = int(pre_value)

    with col2:
        st.markdown(f"#### Korrelation:")
        my_bar = st.progress(0)
        st.markdown(f"# {correl_updated}")
        st.plotly_chart(fig_two)

        for percent_complete in range(bar_value):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1,)
        time.sleep(1)


    fig_three = make_subplots(specs=[[{"secondary_y": True}]])
    fig_three.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=SOL_ONE_DAY, name="Solana"),
        secondary_y=False,
    )
    fig_three.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=ETH_ONE_DAY, name="Ethereum"),
        secondary_y=True,
    )
    fig_three.update_layout(
        title_text=f"Kursvergleich - SOL vs ETH"
    )
    fig_three.update_xaxes(title_text="Zeitraum")
    fig_three.update_yaxes(title_text="Solana", secondary_y=False)
    fig_three.update_yaxes(title_text="Ethereum", secondary_y=True)

    fig, ax = plt.subplots()
    df_updated= df[['SOLANA', 'ETHEREUM']]
    correl= df_updated.corr()
    correl_updated = round(correl.iloc[0,1],2)
    pre_value = correl_updated*100
    bar_value = int(pre_value)




    with col3:
        st.markdown(f"#### Korrelation:")
        my_bar = st.progress(0)

        st.markdown(f"# {correl_updated}")
        st.plotly_chart(fig_three)

        for percent_complete in range(bar_value):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1,)
        time.sleep(1)



#4.4 crypto_prices_4H

SOL_FOUR_HOUR = []
BTC_FOUR_HOUR = []
ETH_FOUR_HOUR= []
Datum_FOUR_HOUR = []


one_week= cur.execute('select * from crypto_prices_4h')
time_frame = one_week.fetchall()

for i in time_frame:
    if 'BTCUSDT' in i:
        x = i[5]
        y = i[1]
        stripped = y[: 10].strip()
        BTC_FOUR_HOUR.append(x)
        Datum_ONE_DAY.append(stripped)
for i in time_frame:
    if 'SOLUSDT' in i:
        x = i[5]
        SOL_FOUR_HOUR.append(x)

for i in time_frame:
    if 'ETHUSDT' in i:
        x = i[5]
        ETH_FOUR_HOUR.append(x)

df_one_day = pd.DataFrame(list(zip(Datum_FOUR_HOUR, BTC_FOUR_HOUR, SOL_FOUR_HOUR, ETH_FOUR_HOUR)),
                      columns=['Datum', 'BITCOIN', 'SOLANA', 'ETHEREUM'])


if option == "crypto_prices_4h":
    #st.column_config.Column(width="large")
    col1, col2, col3 = st.columns([1, 1, 1])

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=BTC_ONE_DAY, name="Bitcoin",fillcolor="#fff"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=SOL_ONE_DAY, name="Solana"),
        secondary_y=True,
    )
    fig.update_layout(
        title_text=f"Kursvergleich - BTC. vs. SOL"
    )
    fig.update_xaxes(title_text="Zeitraum")
    fig.update_yaxes(title_text="Bitcoin", secondary_y=False)
    fig.update_yaxes(title_text="Solana", secondary_y=True)

    df_updated = df[['BITCOIN', 'SOLANA']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)
    pre_value = correl_updated * 100
    bar_value = int(pre_value)

    with col1:
        st.markdown(f"#### Korrelation:")
        my_bar = st.progress(0)
        st.markdown(f"# {correl_updated}")
        st.plotly_chart(fig)
        for percent_complete in range(bar_value):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1,)
        time.sleep(1)



    fig_two = make_subplots(specs=[[{"secondary_y": True}]])
    fig_two.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=BTC_ONE_DAY, name="Bitcoin"),
        secondary_y=False,
    )
    fig_two.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=ETH_ONE_DAY, name="Ethereum"),
        secondary_y=True,
    )
    fig_two.update_layout(
        title_text=f"Kursvergleich - BTC vs.ETH"
    )
    fig_two.update_xaxes(title_text="Zeitraum")
    fig_two.update_yaxes(title_text="Bitcoin", secondary_y=False)
    fig_two.update_yaxes(title_text="Ethereum", secondary_y=True)

    df_updated = df[['BITCOIN', 'ETHEREUM']]
    correl = df_updated.corr()
    correl_updated = round(correl.iloc[0, 1], 2)
    pre_value = correl_updated * 100
    bar_value = int(pre_value)

    with col2:
        st.markdown(f"#### Korrelation:")
        my_bar = st.progress(0)
        st.markdown(f"# {correl_updated}")
        st.plotly_chart(fig_two)

        for percent_complete in range(bar_value):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1,)
        time.sleep(1)


    fig_three = make_subplots(specs=[[{"secondary_y": True}]])
    fig_three.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=SOL_ONE_DAY, name="Solana"),
        secondary_y=False,
    )
    fig_three.add_trace(
        go.Scatter(x=Datum_ONE_DAY, y=ETH_ONE_DAY, name="Ethereum"),
        secondary_y=True,
    )
    fig_three.update_layout(
        title_text=f"Kursvergleich - SOL vs ETH"
    )
    fig_three.update_xaxes(title_text="Zeitraum")
    fig_three.update_yaxes(title_text="Solana", secondary_y=False)
    fig_three.update_yaxes(title_text="Ethereum", secondary_y=True)

    fig, ax = plt.subplots()
    df_updated= df[['SOLANA', 'ETHEREUM']]
    correl= df_updated.corr()
    correl_updated = round(correl.iloc[0,1],2)
    pre_value = correl_updated*100
    bar_value = int(pre_value)




    with col3:
        st.markdown(f"#### Korrelation:")
        my_bar = st.progress(0)

        st.markdown(f"# {correl_updated}")
        st.plotly_chart(fig_three)

        for percent_complete in range(bar_value):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1,)
        time.sleep(1)



connection.close()