import pandas as pd

def calculateRFMSscores(new_dataframe_encoded):
    """
        Calculates RFMS (Recency, Frequency, Monetary, Seasonality) scores for customers.

        Parameters:
            new_dataframe_encoded (pd.DataFrame): Dataset with encoded features.

        Returns:
            pd.DataFrame: Dataset with calculated RFMS scores.
        """
    # Ensure TransactionStartTime is in datetime format
    new_dataframe_encoded['TransactionStartTime'] = pd.to_datetime(new_dataframe_encoded['TransactionStartTime'])

    # Set the current date (or use the last date in your dataset)
    current_date = new_dataframe_encoded['TransactionStartTime'].max()

    # Recency: Number of days since the last transaction
    recency_new_dataframe_encoded = new_dataframe_encoded.groupby('CustomerId').agg({'TransactionStartTime': lambda x: (current_date - x.max()).days})
    recency_new_dataframe_encoded.rename(columns={'TransactionStartTime': 'Recency'}, inplace=True)

    # Frequency: Count of transactions per customer
    frequency_new_dataframe_encoded = new_dataframe_encoded.groupby('CustomerId').agg({'TransactionId': 'count'})
    frequency_new_dataframe_encoded.rename(columns={'TransactionId': 'Frequency'}, inplace=True)

    # Monetary: Sum of transaction amounts per customer
    monetary_new_dataframe_encoded = new_dataframe_encoded.groupby('CustomerId').agg({'Amount': 'sum'})
    monetary_new_dataframe_encoded.rename(columns={'Amount': 'Monetary'}, inplace=True)

    # Seasonality: You can derive this by checking the number of transactions per season (quarter)
    new_dataframe_encoded['Season'] = new_dataframe_encoded['TransactionStartTime'].dt.quarter
    seasonality_new_dataframe_encoded = new_dataframe_encoded.groupby('CustomerId').agg({'Season': 'mean'})
    seasonality_new_dataframe_encoded.rename(columns={'Season': 'Seasonality'}, inplace=True)

    # Merge the dataframes into a single dataframe
    rfms_new_dataframe_encoded = recency_new_dataframe_encoded.merge(frequency_new_dataframe_encoded, on='CustomerId')
    rfms_new_dataframe_encoded = rfms_new_dataframe_encoded.merge(monetary_new_dataframe_encoded, on='CustomerId')
    rfms_new_dataframe_encoded = rfms_new_dataframe_encoded.merge(seasonality_new_dataframe_encoded, on='CustomerId')

    # Normalize the RFMS scores (equal weights for simplicity)
    rfms_new_dataframe_encoded['RFMS_Score'] = (rfms_new_dataframe_encoded['Recency'] * -1 +
                            rfms_new_dataframe_encoded['Frequency'] +
                            rfms_new_dataframe_encoded['Monetary'] +
                            rfms_new_dataframe_encoded['Seasonality'])

    # # Normalize the RFMS scores between 0 and 1
    # rfms_new_dataframe_encoded['RFMS_Score'] = (rfms_new_dataframe_encoded['RFMS_Score'] - rfms_new_dataframe_encoded['RFMS_Score'].min()) / (rfms_new_dataframe_encoded['RFMS_Score'].max() - rfms_new_dataframe_encoded['RFMS_Score'].min())
    return rfms_new_dataframe_encoded