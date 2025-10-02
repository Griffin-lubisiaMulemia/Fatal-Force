import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the poverty and high school completion data
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")

# Convert columns to numeric, coercing errors
df_pct_poverty['poverty_rate'] = pd.to_numeric(df_pct_poverty['poverty_rate'], errors='coerce')
df_pct_completed_hs['percent_completed_hs'] = pd.to_numeric(df_pct_completed_hs['percent_completed_hs'], errors='coerce')

# Aggregate by state (Geographic Area) to get mean values
poverty_by_state = df_pct_poverty.groupby('Geographic Area')['poverty_rate'].mean()
hs_completion_by_state = df_pct_completed_hs.groupby('Geographic Area')['percent_completed_hs'].mean()

# Merge the two series into a single DataFrame for plotting
df_plot = pd.DataFrame({
    'poverty_rate': poverty_by_state,
    'hs_completion_rate': hs_completion_by_state
}).dropna()

# Create a seaborn jointplot with KDE and scatter plot
sns.jointplot(
    data=df_plot,
    x='poverty_rate',
    y='hs_completion_rate',
    kind='scatter',  # scatter plot with KDE contours by default
    marginal_kws=dict(bins=25, fill=True),
    height=8,
    space=0.3
).plot_joint(sns.kdeplot, zorder=0, levels=6)

plt.suptitle('Relationship between Poverty Rate and High School Completion Rate by State', y=1.02)
plt.xlabel('Average Poverty Rate (%)')
plt.ylabel('Average High School Completion Rate (%)')
plt.show()
