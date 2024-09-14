import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('../../datasets/latest_nvidia_data.csv', index_col=0)
data = data.iloc[:10, :]

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Create a heatmap
sns.heatmap(data, annot=True, cmap='YlGnBu', linewidths=.5)

# Add title and labels
plt.title('Heatmap Example')
plt.xlabel('Day of the Week')
plt.ylabel('Time of Day')

# Show the plot
plt.show()