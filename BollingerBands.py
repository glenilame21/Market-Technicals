def bollingerbands(df, window=20,sd =2):
    #df['MA'] = df['Close'].rolling(window=window).mean()
    df['BB_up'] = df['SMA'] + (df['Close'].rolling(window=window).std() * sd)
    df['BB_down'] = df['SMA'] - (df['Close'].rolling(window=window).std() * sd)
    return df