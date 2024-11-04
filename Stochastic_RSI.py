def calculate_stochastic_rsi(df, rsi_period=14, stoch_period=14, smooth_k=3, smooth_d=3):
    # Calculate the lowest RSI and highest RSI over the specified period
    df['RSI_Low'] = df['RSI'].rolling(window=stoch_period).min()
    df['RSI_High'] = df['RSI'].rolling(window=stoch_period).max()
    
    # Calculate Stochastic RSI
    df['Stoch_RSI'] = (df['RSI'] - df['RSI_Low']) / (df['RSI_High'] - df['RSI_Low']) 
    return df