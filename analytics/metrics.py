"""
Core metrics calculation module.
These functions are used by the AI Agent to answer metric-related questions.
"""
import pandas as pd
import numpy as np

def calculate_total_deliveries(df: pd.DataFrame) -> int:
    """Calculate total number of deliveries."""
    return len(df)

def calculate_delivery_time_stats(df: pd.DataFrame) -> dict:
    """Calculate average, median, and P90 delivery times."""
    # Filter out invalid delivery times just in case
    valid_times = df[df['time_taken_min'] > 0]['time_taken_min']
    
    return {
        'mean': round(valid_times.mean(), 2),
        'median': round(valid_times.median(), 2),
        'p90': round(valid_times.quantile(0.90), 2),
        'std_dev': round(valid_times.std(), 2),
        'count': len(valid_times)
    }

def calculate_pickup_delay_stats(df: pd.DataFrame) -> dict:
    """Calculate pickup delay statistics."""
    valid_delays = df[df['pickup_delay_minutes'].notna()]['pickup_delay_minutes']
    
    if len(valid_delays) == 0:
        return {'mean': 0, 'median': 0, 'count': 0}
        
    return {
        'mean': round(valid_delays.mean(), 2),
        'median': round(valid_delays.median(), 2),
        'count': len(valid_delays)
    }

def calculate_operational_percentages(df: pd.DataFrame) -> dict:
    """Calculate percentages for high traffic, multiple deliveries, and poor vehicle condition."""
    total = len(df)
    
    high_traffic = len(df[df['road_traffic_density'].isin(['High', 'Jam'])])
    multiple_deliveries = len(df[df['multiple_deliveries'] > 0])
    poor_vehicle = len(df[df['vehicle_condition'] == 0])
    
    return {
        'high_traffic_pct': round((high_traffic / total) * 100, 2),
        'multiple_deliveries_pct': round((multiple_deliveries / total) * 100, 2),
        'poor_vehicle_condition_pct': round((poor_vehicle / total) * 100, 2)
    }