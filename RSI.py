import pandas as pd

def calculate_rsi(data, period=14, column='Close'):
    delta = data[column].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def RSI_signal(df):
    df['RSI_Signal'] = pd.cut(df['RSI'], 
                              bins=[-float('inf'), 30, 70, float('inf')],
                              labels=['Bearish', 'Neutral', 'Bullish'])
    return df