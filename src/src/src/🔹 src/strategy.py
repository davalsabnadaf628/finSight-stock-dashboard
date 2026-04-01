def moving_average_strategy(df):
    df['MA50'] = df['Close'].rolling(50).mean()
    df['Signal'] = 0

    df.loc[df['Close'] < df['MA50'], 'Signal'] = 1
    df.loc[df['Close'] > df['MA50'], 'Signal'] = -1

    return df
