import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('/content/unemployement rate.csv')
data.columns = data.columns.str.strip()  # Strip whitespace from column names

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the date as the index
data.set_index('Date', inplace=True)

# Overview of the dataset
print(data.head())

# Visualizing the Unemployment Rate over time with Seaborn
plt.figure(figsize=(14, 7))
sns.lineplot(data=data, x=data.index, y='Estimated Unemployment Rate (%)', label='Unemployment Rate', color='blue')
plt.axvline(pd.to_datetime('2020-03-01'), color='red', linestyle='--', label='COVID-19 Start')
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.legend()
plt.grid()
plt.savefig('unemployment_rate_analysis.png')  # Save the plot before showing
plt.show()

# Identify peak unemployment rate during COVID-19
peak_rate = data['Estimated Unemployment Rate (%)'].max()
peak_date = data['Estimated Unemployment Rate (%)'].idxmax()
print(f"Peak Unemployment Rate: {peak_rate}% on {peak_date.date()}")

# Comparing pre-COVID and post-COVID rates
pre_covid = data[data.index < pd.to_datetime('2020-03-01')]
post_covid = data[data.index >= pd.to_datetime('2020-03-01')]

print(f"Average Pre-COVID Unemployment Rate: {pre_covid['Estimated Unemployment Rate (%)'].mean():.2f}%")
print(f"Average Post-COVID Unemployment Rate: {post_covid['Estimated Unemployment Rate (%)'].mean():.2f}%")

# Optional: Demographic analysis if additional columns are available
# If the dataset includes demographics, you could use:
# demographic_data = pd.read_csv('unemployment_demographics.csv')
# demographic_data.groupby('Demographic_Group')['Unemployment_Rate'].mean().plot(kind='bar')
