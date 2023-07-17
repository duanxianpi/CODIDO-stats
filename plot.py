import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

# Load your data
df = pd.read_csv('stats.csv')

# Convert the 'Timestamp' column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s') - pd.Timedelta('05:00:00')

# Get last 5 days of the data
df =  df[df['Timestamp'] > df['Timestamp'].max() - pd.Timedelta(days=5)]

plot_names = []
for name,group in df.groupby('Name')['Runs']:
    if group.max() > group.min():
        plot_names.append(name)

# Get the rows with the algorithms in plot_names
df = df[df['Name'].isin(plot_names)]

df.sort_values(['Timestamp', 'Name'], inplace=True)
fig, ax = plt.subplots(figsize=(16,9))

# Group the data by 'Name' and plot each group
for name, group in df.groupby('Name'):
    group.plot(x='Timestamp', y='Runs', ax=ax, label=name)

# # Set the x-axis to have a tick every 6 hours
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=720))

# Set the x-axis to have a tick every day, formatting the tick labels as 'June 15'
ax.xaxis.set_major_formatter(DateFormatter("%m/%d %H:%M"))

plt.xlabel('Time (In EST)')
plt.ylabel('Runs')
plt.title('Trend of Runs over Time')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

# plt.gca().legend_ = None

# Save the figure 1920x1080
plt.savefig('plot.svg', dpi=120,bbox_inches='tight',format='svg')
