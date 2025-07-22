import os
os.makedirs('visuals', exist_ok=True)


import matplotlib.pyplot as plt

def plot_churn_pie(df):
    counts = df['Churn'].value_counts()
    labels = ['Retained', 'Churned']
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140, explode=(0.05, 0.1), shadow=True)
    plt.title('Churn vs. Retention')
    plt.savefig('visuals/churn_vs_retention_pie.png')
    plt.close()

import seaborn as sns

def plot_roi_by_channel(df):
    roi_df = df.groupby('Channel')[['Revenue', 'Ad_Spend']].sum()
    roi_df['ROI'] = (roi_df['Revenue'] - roi_df['Ad_Spend']) / roi_df['Ad_Spend']
    roi_df = roi_df.reset_index()

    plt.figure(figsize=(8, 5))
    sns.barplot(x='Channel', y='ROI', data=roi_df)
    plt.title('ROI by Marketing Channel')
    plt.ylabel('ROI')
    plt.xlabel('Channel')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visuals/roi_by_channel.png')
    plt.close()

def plot_adspend_vs_revenue(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Ad_Spend', y='Revenue', hue='Channel', data=df)
    plt.title('Ad Spend vs Revenue')
    plt.xlabel('Ad Spend')
    plt.ylabel('Revenue')
    plt.tight_layout()
    plt.savefig('visuals/adspend_vs_revenue_scatter.png')
    plt.close()

def plot_cltv_heatmap(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Prepare data for heatmap
    cltv_grouped = df.groupby(['Age_Group', 'Income_Group'])['CLTV'].mean().reset_index()

    # Pivot for heatmap
    pivot = cltv_grouped.pivot(index='Age_Group', columns='Income_Group', values='CLTV')

    # Plot
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap='YlGnBu', cbar_kws={'label': 'Avg CLTV'})
    plt.title('Average CLTV by Age Group and Income Group')
    plt.xlabel('Income Group')
    plt.ylabel('Age Group')
    plt.tight_layout()
    plt.savefig('visuals/cltv_heatmap.png')
    plt.close()

def plot_cltv_by_channel(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='Channel', y='CLTV')
    plt.title('CLTV Distribution by Channel')
    plt.xlabel('Marketing Channel')
    plt.ylabel('Customer Lifetime Value (CLTV)')
    plt.tight_layout()
    plt.savefig('visuals/cltv_by_channel_boxplot.png')
    plt.close()


def plot_avg_roi_by_channel(df):
    roi_df = df.groupby('Channel')['ROI'].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=roi_df, x='Channel', y='ROI')
    plt.title('Average ROI by Channel')
    plt.ylabel('Average ROI')
    plt.xlabel('Marketing Channel')
    plt.tight_layout()
    plt.savefig('visuals/avg_roi_by_channel.png')
    plt.close()

def plot_income_vs_cltv(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='Income', y='CLTV', hue='Channel')
    plt.title('Income vs CLTV by Channel')
    plt.xlabel('Income')
    plt.ylabel('Customer Lifetime Value')
    plt.tight_layout()
    plt.savefig('visuals/income_vs_cltv.png')
    plt.close()

def plot_kpi_correlation_heatmap(df):
    corr_fields = ['Income', 'CLTV', 'Revenue', 'Ad_Spend', 'ROI', 'Tenure_Months']
    corr_matrix = df[corr_fields].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Between Key Marketing KPIs')
    plt.tight_layout()
    plt.savefig('visuals/kpi_correlation_heatmap.png')
    plt.close()


def plot_channel_financials(df):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    data = {
        'Channel': ['Phone', 'Email', 'SMS', 'Social Media'],
        'Revenue': [751995.23, 595564.39, 353256.35, 195859.38],
        'Ad_Spend': [45266.90, 34378.99, 21363.47, 12194.01],
        'Profit': [706728.33, 561185.40, 331892.88, 183665.38]
    }

    df = pd.DataFrame(data)

    
    df_melted = df.melt(id_vars='Channel', value_vars=['Revenue', 'Ad_Spend', 'Profit'],
                        var_name='Metric', value_name='Amount')

    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Channel', y='Amount', hue='Metric', data=df_melted)

    plt.title('Financial Overview by Marketing Channel')
    plt.ylabel('Amount ($)')
    plt.xlabel('Marketing Channel')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.legend(title='Financial Metric')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('visuals/channel_financials_comparison.png')
    plt.show()


if __name__ == "__main__":
    import pandas as pd
    from scripts import metrics

    visuals_df = pd.read_csv('/Users/Darshan/Desktop/Projects/Marketing_analysis_roi/data/marketing_enhanced.csv')

    visuals_df = metrics.calculate_cltv(visuals_df)
    visuals_df = metrics.calculate_roi(visuals_df)

    plot_churn_pie(visuals_df)
    plot_roi_by_channel(visuals_df)
    plot_adspend_vs_revenue(visuals_df)
    plot_cltv_heatmap(visuals_df)
    plot_cltv_by_channel(visuals_df)
    plot_avg_roi_by_channel(visuals_df)
    plot_income_vs_cltv(visuals_df)
    plot_kpi_correlation_heatmap(visuals_df)
    plot_channel_financials(visuals_df)

    print("Charts saved in visuals folder")
