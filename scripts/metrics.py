import pandas as pd

def calculate_cac(df):
    total_spend = df['Ad_Spend'].sum()
    total_conversions = df['Response'].sum()
    return round(total_spend / total_conversions, 2)

def calculate_cltv(df):
    df['CLTV'] = df['Revenue'] * df['Tenure_Months']
    return df

def calculate_roi(df):
    df['ROI'] = (df['Revenue'] - df['Ad_Spend']) / df['Ad_Spend']
    return df

def churn_rate(df):
    return round(df['Churn'].mean() * 100, 2)

def profit_by_channel(df):
    result = df.groupby('Channel')[['Revenue', 'Ad_Spend']].sum()
    result['Profit'] = result['Revenue'] - result['Ad_Spend']
    return result.sort_values('Profit', ascending=False)
