"""
Period comparison and effect size calculation module.
Used to compare metrics across different time periods or segments.
"""
import pandas as pd
import numpy as np
from scipy import stats

def compare_periods(df: pd.DataFrame, period_col: str, metric_col: str, 
                    period_1_val: str, period_2_val: str) -> dict:
    """
    Compare a specific metric between two periods (e.g., Month 1 vs Month 2).
    
    Args:
        df: The analytical dataframe.
        period_col: The column defining the period (e.g., 'month').
        metric_col: The metric to compare (e.g., 'time_taken_min').
        period_1_val: The baseline period value (e.g., 'February').
        period_2_val: The current period value (e.g., 'March').
    """
    # Filter data for both periods
    p1_data = df[df[period_col] == period_1_val][metric_col].dropna()
    p2_data = df[df[period_col] == period_2_val][metric_col].dropna()
    
    if len(p1_data) == 0 or len(p2_data) == 0:
        return {'error': 'One or both periods have no valid data.'}
    
    # Calculate statistics
    p1_mean = p1_data.mean()
    p2_mean = p2_data.mean()
    
    abs_change = p2_mean - p1_mean
    pct_change = (abs_change / p1_mean) * 100 if p1_mean != 0 else 0
    
    # Statistical significance (T-test)
    t_stat, p_value = stats.ttest_ind(p1_data, p2_data, equal_var=False)
    is_significant = p_value < 0.05
    
    # Effect size (Cohen's d)
    pooled_std = np.sqrt(((len(p1_data) - 1) * p1_data.std()**2 + (len(p2_data) - 1) * p2_data.std()**2) / (len(p1_data) + len(p2_data) - 2))
    cohens_d = abs_change / pooled_std if pooled_std != 0 else 0
    
    return {
        'period_1': {
            'name': period_1_val,
            'mean': round(p1_mean, 2),
            'count': len(p1_data)
        },
        'period_2': {
            'name': period_2_val,
            'mean': round(p2_mean, 2),
            'count': len(p2_data)
        },
        'absolute_change': round(abs_change, 2),
        'percentage_change': round(pct_change, 2),
        'statistical_significance': {
            'p_value': round(p_value, 4),
            'is_significant': is_significant
        },
        'effect_size': {
            'cohens_d': round(cohens_d, 4),
            'interpretation': 'Small' if abs(cohens_d) < 0.5 else ('Medium' if abs(cohens_d) < 0.8 else 'Large')
        }
    }

def segment_analysis(df: pd.DataFrame, segment_col: str, metric_col: str) -> pd.DataFrame:
    """
    Analyze a metric across different segments (e.g., Delivery Time by City).
    """
    result = df.groupby(segment_col)[metric_col].agg(['mean', 'median', 'count', 'std']).reset_index()
    result.columns = [segment_col, 'mean', 'median', 'count', 'std_dev']
    
    # Sort by mean descending to show worst performers first
    result = result.sort_values('mean', ascending=False).reset_index(drop=True)
    
    # Round values
    for col in ['mean', 'median', 'std_dev']:
        result[col] = result[col].round(2)
        
    return result