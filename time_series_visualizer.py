



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# ✅ Import data and set 'date' as index
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# ✅ Remove top 2.5% and bottom 2.5% of data
lower_bound = df["value"].quantile(0.025)  # Bottom 2.5%
upper_bound = df["value"].quantile(0.975)  # Top 2.5%
df = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]

# ✅ Display the first few rows and check size
print(df.head())
print(f"Dataset size after cleaning: {df.shape}")

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 5))  # Create a figure and axis

    ax.plot(df.index, df['value'], color='red', linewidth=1)  # Line plot
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")  # Title
    ax.set_xlabel("Date")  # X-axis label
    ax.set_ylabel("Page Views")  # Y-axis label

    fig.savefig('line_plot.png')  # Save figure
    return fig  # Return figure


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Create pivot table for bar chart
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot bar chart
    df_bar.plot(kind="bar", ax=ax)

    # Set labels and title
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Average Daily Page Views per Month")

    # Set legend title
    ax.legend(title="Months", labels=[
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
         ])

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig

# Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year  
    df_box['month'] = df_box['date'].dt.strftime('%b')  # Short month names

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    #  Force save
    fig.savefig('box_plot.png', bbox_inches='tight', dpi=300)

    return fig

 # Make sure this is properly indented

