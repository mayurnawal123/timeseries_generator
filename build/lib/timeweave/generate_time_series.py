import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_time_series(trend_type, sub_option=None, start_time='2020-01-01', num_points=100, granularity='day', data_range=(0, 100)):
    start_time = datetime.strptime(start_time, '%Y-%m-%d')
    time_deltas = {'minute': timedelta(minutes=1), 'hour': timedelta(hours=1), 'day': timedelta(days=1), 
                   'month': timedelta(days=30), 'year': timedelta(days=365)}
    
    dates = [start_time + i * time_deltas[granularity] for i in range(num_points)]
    x = np.arange(num_points)
    min_val, max_val = data_range
    
    if trend_type == 'linear':
        data = np.linspace(min_val, max_val, num_points)
    elif trend_type == 'polynomial':
        if sub_option == 'quadratic':
            data = np.linspace(min_val, max_val, num_points) ** 2
        elif sub_option == 'cubic':
            data = np.linspace(min_val, max_val, num_points) ** 3
        else:
            raise ValueError("Invalid sub_option for polynomial trend. Choose 'quadratic' or 'cubic'.")
    elif trend_type == 'exponential':
        data = np.exp(np.linspace(min_val, max_val, num_points))
    elif trend_type == 'logarithmic':
        data = np.log(np.linspace(min_val + 1, max_val + 1, num_points))
    elif trend_type == 'sinusoidal':
        data = np.sin(2 * np.pi * np.linspace(min_val, max_val, num_points))
    elif trend_type == 'logistic':
        L, k, x0 = 1, 0.1, num_points / 2
        data = L / (1 + np.exp(-k * (x - x0)))
    elif trend_type == 'power_law':
        data = (np.linspace(min_val, max_val, num_points)) ** 2
    elif trend_type == 'moving_average':
        data = np.convolve(np.random.randn(num_points), np.ones(10)/10, mode='valid')
        dates = dates[:len(data)]
    else:
        raise ValueError("Invalid trend_type. Choose 'linear', 'polynomial', 'exponential', 'logarithmic', 'sinusoidal', 'logistic', 'power_law', or 'moving_average'.")
    
    return pd.DataFrame({'Date': dates, 'Value': data})
