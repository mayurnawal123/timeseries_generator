import pandas as pd
from timeweave import generate_time_series

def generate_time_series_from_config(config):
    trend_config = config.get('trend', {})
    trend_type = trend_config.get('trend_type')
    sub_option = trend_config.get('sub_option')
    start_time = trend_config.get('start_time')
    num_points = trend_config.get('num_points')
    granularity = trend_config.get('granularity')
    data_range = trend_config.get('data_range', [0, 100])
    df = generate_time_series(trend_type, sub_option, start_time, num_points, granularity, data_range)
    return df

def plot_time_series(df, title="Generated Time Series"):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Value'])
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    config_file = {
      "trend": {
        "trend_type": "linear",
        "sub_option": None,
        "start_time": "2023-01-01",
        "num_points": 200,
        "granularity": "day",
        "data_range": [0, 100]
      }
    }

    df = generate_time_series_from_config(config_file)
    plot_time_series(df, title="Generated Time Series")
