def cal_SMA(df , period = 20 ):

    df['SMA'] = df['Close'].rolling(window=period).mean()
    return df