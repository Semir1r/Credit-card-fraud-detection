import pandas as pd
import numpy as np

def calculate_woe_iv(data, feature, target):
    """
       Calculates Weight of Evidence (WoE) and Information Value (IV) for a given feature.

       Parameters:
           data (pd.DataFrame): Dataset containing the feature and target variable.
           feature (str): The feature column to analyze.
           target (str): The target variable column.

       Returns:
           pd.DataFrame: DataFrame with unique values, WoE, and IV for the feature.
       """
    lst = []
    unique_values = data[feature].unique()
    total_good = len(data[data[target] == 1])
    total_bad = len(data[data[target] == 0])

    for val in unique_values:
        dist_good = len(data[(data[feature] == val) & (data[target] == 1)]) / total_good if total_good != 0 else 0
        dist_bad = len(data[(data[feature] == val) & (data[target] == 0)]) / total_bad if total_bad != 0 else 0

        # Handle cases where dist_good or dist_bad is zero
        if dist_good == 0:
            dist_good = 0.0001
        if dist_bad == 0:
            dist_bad = 0.0001

        woe = np.log(dist_good / dist_bad)
        iv = (dist_good - dist_bad) * woe
        lst.append({'Value': val, 'WoE': woe, 'IV': iv})

    return pd.DataFrame(lst)