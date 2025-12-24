import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
file_path = '/home/ubuntu/upload/Tesla_Stock_Data_with_Technical_and_Social_Features_2015_2020.csv'
df = pd.read_csv(file_path)

# 2. Convert Date to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# 3. Visualization - Matching the Screenshot Style
plt.figure(figsize=(12, 5))

# Plot the compound sentiment as a green line
plt.plot(df['Date'], df['compound'], color='green', linewidth=1, label='Elon Musk Compound Sentiment')

# Add the vertical red dashed line for Train/Test Split (at 2019-01-01)
split_date = pd.to_datetime('2019-01-01')
plt.axvline(x=split_date, color='red', linestyle='--', linewidth=1.5, label='Train/Test Split')

# Set labels and title to match the screenshot
plt.title('Elon Musk Twitter Compound Sentiment Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Compound Sentiment Score', fontsize=12)

# Set y-axis limits to match the screenshot (-1.0 to 1.0)
plt.ylim(-1.0, 1.0)

# Add grid for better readability
plt.grid(True, which='both', linestyle='-', alpha=0.3)

# Add legend at the bottom left
plt.legend(loc='lower left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('/home/ubuntu/sentiment_over_time_recreated.png', dpi=300)
print("Sentiment plot recreated successfully as sentiment_over_time_recreated.png")
