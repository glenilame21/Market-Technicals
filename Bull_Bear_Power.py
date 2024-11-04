def calculate_bull_bear_power(df, period=13):
    # Calculate the Exponential Moving Average (EMA)
    df['EMA'] = df['Close'].ewm(span=period, adjust=False).mean()
    
    # Calculate Bull Power
    df['Bull_Power'] = df['High'] - df['EMA']
    
    # Calculate Bear Power
    df['Bear_Power'] = df['Low'] - df['EMA']
    
    return df



##########################################################################################################################################

#### Buy signal: Bulls Power is growing above the zero line. Bears Power is below the zero line, and the bars are decreasing.#############

#### Sell signal: Bulls Power is above the zero line, the bars are falling. Bears Power is below the zero line, the bars are decreasing.##

##########################################################################################################################################
def generate_bulls_bears_signals(data):
    data['BullsPower_Growing'] = data['Bull_Power'].diff() > 0
    data['BearsPower_Decreasing'] = data['Bear_Power'].diff() < 0
    
    data['BullBearPower_Buy_Signal'] = (data['Bull_Power'] > 0) & (data['BullsPower_Growing']) & (data['Bear_Power'] < 0) & (data['BearsPower_Decreasing'])
    data['BullBearPower_Sell_Signal'] = (data['Bull_Power'] > 0) & (~data['BullsPower_Growing']) & (data['Bear_Power'] < 0) & (data['BearsPower_Decreasing'])
    
    return data


