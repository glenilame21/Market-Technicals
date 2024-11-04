def calculate_cci(df, n=20):
    # Calculate the Typical Price (TP)
    TP = (df['High'] + df['Low'] + df['Close']) / 3
    
    # Calculate the Simple Moving Average (SMA) of TP
    SMA = TP.rolling(window=n).mean()
    
    # Calculate the Mean Deviation
    def mean_deviation(series):
        mean = series.mean()
        return (series - mean).abs().mean()
    
    mean_deviation = TP.rolling(window=n).apply(mean_deviation)
    
    # Calculate the CCI
    CCI = (TP - SMA) / (0.015 * mean_deviation)
    
    # Add the CCI to the DataFrame
    df['CCI'] = CCI
    
    return df