"""
Analytics Tools for the AI Agent.
These functions perform the actual data calculations.
"""
import pandas as pd
from pathlib import Path

# Load the cleaned data once when the module is imported
DATA_PATH = Path(__file__).parent.parent / "data" / "processed" / "zomato_cleaned_analytical.csv"
df = pd.read_csv(DATA_PATH)

def get_metric_overview() -> dict:
    """Returns high-level KPIs for the dataset."""
    return {
        "total_deliveries": len(df),
        "avg_delivery_time": round(df['time_taken_min'].mean(), 2),
        "median_delivery_time": round(df['time_taken_min'].median(), 2),
        "date_range": f"{df['order_date'].min()} to {df['order_date'].max()}"
    }

def segment_by_column(column: str, metric: str = 'time_taken_min') -> dict:
    """
    Groups data by a categorical column and calculates the mean of a metric.
    Example: segment_by_column('road_traffic_density', 'time_taken_min')
    """
    if column not in df.columns:
        return {"error": f"Column {column} not found."}
    
    result = df.groupby(column)[metric].agg(['mean', 'count']).round(2)
    return result.to_dict(orient='index')

def compare_months(month_1: int, month_2: int, metric: str = 'time_taken_min') -> dict:
    """Compares a metric between two months."""
    m1_data = df[df['month'] == month_1][metric]
    m2_data = df[df['month'] == month_2][metric]
    
    return {
        f"Month_{month_1}_avg": round(m1_data.mean(), 2),
        f"Month_{month_1}_count": len(m1_data),
        f"Month_{month_2}_avg": round(m2_data.mean(), 2),
        f"Month_{month_2}_count": len(m2_data),
        "absolute_change": round(m2_data.mean() - m1_data.mean(), 2)
    }

# Registry of available tools for the LLM
AVAILABLE_TOOLS = {
    "get_metric_overview": {
        "description": "Get high-level KPIs like total deliveries and average delivery time.",
        "function": get_metric_overview
    },
    "segment_by_column": {
        "description": "Analyze a metric broken down by a category (e.g., city, traffic, weather).",
        "function": segment_by_column
    },
    "compare_months": {
        "description": "Compare a metric between two specific months (e.g., 2 for Feb, 3 for Mar).",
        "function": compare_months
    }
}