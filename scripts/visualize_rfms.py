import matplotlib.pyplot as plt

def visualizeRFMSscore(rfms_new_dataframe_encoded):
    """
       Visualizes RFMS scores as a histogram.

       Parameters:
           rfms_new_dataframe_encoded (pd.DataFrame): Dataset containing RFMS scores.
       """
    # Plot the histogram of RFMS scores
    plt.figure(figsize=(8,6))
    plt.hist(rfms_new_dataframe_encoded['RFMS_Score'], bins=30, color='blue', alpha=0.7)
    plt.title('RFMS Score Distribution')
    plt.xlabel('RFMS Score')
    plt.ylabel('Frequency')
    plt.show()
    