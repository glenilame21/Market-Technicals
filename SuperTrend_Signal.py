def supertrend_signals(df):
    df['Bullish_Signal'] = False
    df['Bearish_Signal'] = False
    
    for i in range(1, len(df)):
        # Bullish Signal
        if df['Supertrend'][i-1] > df['Close'][i-1] and df['Supertrend'][i] < df['Close'][i]:
            df.at[i, 'Supertrend_Bullish_Signal'] = True
        
        # Bearish Signal
        if df['Supertrend'][i-1] < df['Close'][i-1] and df['Supertrend'][i] > df['Close'][i]:
            df.at[i, 'Supertrend_Bearish_Signal'] = True
    
    return df