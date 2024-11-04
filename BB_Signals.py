def bb_signals(df):
    df['Bullish_Bounce'] = False
    df['Bullish_W_Bottom'] = False
    df['Bullish_Walking_Lower_Band'] = False
    df['Bullish_Squeeze_Upward_Breakout'] = False
    df['Bearish_Rejection'] = False
    df['Bearish_M_Top'] = False
    df['Bearish_Walking_Upper_Band'] = False
    df['Bearish_Squeeze_Downward_Breakout'] = False
    
    for i in range(1, len(df)):
        # Bullish Signals
        if df['Close'][i-1] < df['BB_down'][i-1] and df['Close'][i] > df['BB_down'][i]:
            df.at[i, 'Bullish_Bounce'] = True
        
        if i > 1 and df['Close'][i-2] < df['BB_down'][i-2] and df['Close'][i] < df['BB_down'][i] and df['Close'][i-1] > df['BB_down'][i-1]:
            df.at[i, 'Bullish_W_Bottom'] = True
        
        if df['Close'][i] < df['BB_down'][i] and df['Close'][i-1] < df['BB_down'][i-1]:
            df.at[i, 'Bullish_Walking_Lower_Band'] = True
        
        if i > 1 and (df['BB_up'][i] - df['BB_down'][i]) < (df['BB_up'][i-1] - df['BB_down'][i-1]) and df['Close'][i] > df['BB_up'][i]:
            df.at[i, 'Bullish_Squeeze_Upward_Breakout'] = True
        
        # Bearish Signals
        if df['Close'][i-1] > df['BB_up'][i-1] and df['Close'][i] < df['BB_up'][i]:
            df.at[i, 'Bearish_Rejection'] = True
        
        if i > 1 and df['Close'][i-2] > df['BB_up'][i-2] and df['Close'][i] > df['BB_up'][i] and df['Close'][i-1] < df['BB_up'][i-1]:
            df.at[i, 'Bearish_M_Top'] = True
        
        if df['Close'][i] > df['BB_up'][i] and df['Close'][i-1] > df['BB_up'][i-1]:
            df.at[i, 'Bearish_Walking_Upper_Band'] = True
        
        if i > 1 and (df['BB_up'][i] - df['BB_down'][i]) < (df['BB_up'][i-1] - df['BB_down'][i-1]) and df['Close'][i] < df['BB_down'][i]:
            df.at[i, 'Bearish_Squeeze_Downward_Breakout'] = True
    
    return df