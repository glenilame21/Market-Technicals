import pandas as pd

def CCI_BB_Signal(df):
    df['CCI_Bullish_Signal'] = 0
    df['CCI_Bearish_Signal'] = 0

    for i in range(1, len(df)):
        # Bullish signals
        if df['CCI'].iloc[i-1] < -100 and df['CCI'].iloc[i] > -100:
            df.at[i, 'CCI_Bullish_Signal'] = 1
        if df['CCI'].iloc[i-1] < 0 and df['CCI'].iloc[i] > 0:
            df.at[i, 'CCI_Bullish_Signal'] = 1
        if df['Close'].iloc[i] < df['Close'].iloc[i-1] and df['CCI'].iloc[i] > df['CCI'].iloc[i-1]:
            df.at[i, 'CCI_Bullish_Signal'] = 1

        # Bearish signals
        if df['CCI'].iloc[i-1] > 100 and df['CCI'].iloc[i] < 100:
            df.at[i, 'CCI_Bearish_Signal'] = 1
        if df['CCI'].iloc[i-1] > 0 and df['CCI'].iloc[i] < 0:
            df.at[i, 'CCI_Bearish_Signal'] = 1
        if df['Close'].iloc[i] > df['Close'].iloc[i-1] and df['CCI'].iloc[i] < df['CCI'].iloc[i-1]:
            df.at[i, 'CCI_Bearish_Signal'] = 1

    return df