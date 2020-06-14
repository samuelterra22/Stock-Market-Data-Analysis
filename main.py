import plotly.offline as py
import plotly.io as pio
import plotly.graph_objs as go
import yfinance as yf

market = "MEAL3.SA"

df = yf.download(market, group_by="ticker", start="2020-01-01")  # end=date.today()

pio.renderers.default = "iframe"

# Simple means
df['MM_3'] = df.Close.rolling(window=3).mean()  # Mean of 3 days
df['MM_7'] = df.Close.rolling(window=7).mean()  # Mean of 7 days
df['MM_21'] = df.Close.rolling(window=21).mean()  # Mean of 21 days

MM_3 = go.Scatter(
    x=df.index,
    y=df['MM_3'],
    name='MM 3 days',
    line=dict(color='#330000'),
    opacity=0.8)

MM_7 = go.Scatter(
    x=df.index,
    y=df['MM_7'],
    name='MM 7 days',
    line=dict(color='#b51fda'),
    opacity=0.8)

MM_21 = go.Scatter(
    x=df.index,
    y=df['MM_21'],
    name='MM 21 days',
    line=dict(color='#00FF00'),
    opacity=0.8)

# Candlestick
trace = go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    increasing=dict(line=dict(color='#2ebd84')),
    decreasing=dict(line=dict(color='#e0294a')))

close = go.Scatter(
    x=df.index,
    y=df.Close,
    name='PETR4.SA Close',
    line=dict(color='#330000'),
    opacity=0.8)

data = [trace, MM_3, MM_7, MM_21]

layout = go.Layout(
        title='Stock Market Data Analysis - ' + market,
        yaxis=dict(
            title='Stock market price',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        xaxis=dict(
            title='Date',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )

figure = {'data': data, 'layout': layout}

py.plot(figure, filename='candlestick.html')