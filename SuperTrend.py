import pandas as pd

def calculate_atr(df, period=14):
    df['H-L'] = abs(df['High'] - df['Low'])
    df['H-PC'] = abs(df['High'] - df['Close'].shift(1))
    df['L-PC'] = abs(df['Low'] - df['Close'].shift(1))
    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)
    df['ATR'] = df['TR'].rolling(window=period).mean()
    return df

def calculate_supertrend(df, period=14, multiplier=3):
    df = calculate_atr(df, period)
    df['Basic Upper Band'] = (df['High'] + df['Low']) / 2 + (multiplier * df['ATR'])
    df['Basic Lower Band'] = (df['High'] + df['Low']) / 2 - (multiplier * df['ATR'])
    
    df['Final Upper Band'] = 0.0
    df['Final Lower Band'] = 0.0
    df['Supertrend'] = 0.0
    
    for i in range(period, len(df)):
        if df['Close'][i-1] <= df['Final Upper Band'][i-1]:
            df['Final Upper Band'][i] = min(df['Basic Upper Band'][i], df['Final Upper Band'][i-1])
        else:
            df['Final Upper Band'][i] = df['Basic Upper Band'][i]
        
        if df['Close'][i-1] >= df['Final Lower Band'][i-1]:
            df['Final Lower Band'][i] = max(df['Basic Lower Band'][i], df['Final Lower Band'][i-1])
        else:
            df['Final Lower Band'][i] = df['Basic Lower Band'][i]
        
        if df['Close'][i] <= df['Final Upper Band'][i]:
            df['Supertrend'][i] = df['Final Upper Band'][i]
        else:
            df['Supertrend'][i] = df['Final Lower Band'][i]
    
    return df