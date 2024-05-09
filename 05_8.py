import pandas as pd
import matplotlib.pyplot as plt

path_to_file = "C:/Users/haris/Downloads/t20_stats.csv - Sheet1.csv"

# Read the CSV file
df = pd.read_csv(path_to_file)

# Set the first column as the index (assuming it contains the names of the statistics)
df.set_index(df.columns[0], inplace=True)

# Get the statistics for each player
virat_stats = df['Virat Kohli']
babar_stats = df['Babar Azam']

print(babar_stats)
# Create a new DataFrame to store the comparison
comparison_df = pd.DataFrame({'Virat Kohli': virat_stats, 'Babar Azam': babar_stats})
print(comparison_df)
# Identify rows where Babar Azam's statistics are better than Virat Kohli's
better_rows = babar_stats > virat_stats

print(better_rows)

# Plot the trend
plt.figure(figsize=(15, 9))
comparison_df.plot(kind='bar')
plt.title('Virat Kohli vs. Babar Azam')
plt.xlabel('Statistics')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.tight_layout()

# Highlight rows where Babar Azam is better than Virat Kohli
for i, better_row in enumerate(better_rows):
    if better_row:
        plt.axvline(x=i, color='red', linestyle='--')

plt.show()
