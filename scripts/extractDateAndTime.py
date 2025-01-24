import pandas as pd

def extractDateAndTime(new_dataframe):
    """
        Extracts date and time features from a datetime column.

        Parameters:
            new_dataframe (pd.DataFrame): Dataset containing a datetime column 'TransactionStartTime'.

        Returns:
            pd.DataFrame: Dataset with new time-based features.
        """
    # Converting TransactionStartTime to datetime format
    new_dataframe['TransactionStartTime'] = pd.to_datetime(new_dataframe['TransactionStartTime'])

    # Extracting date and time-based features
    new_dataframe['TransactionHour'] = new_dataframe['TransactionStartTime'].dt.hour
    new_dataframe['TransactionDay'] = new_dataframe['TransactionStartTime'].dt.day
    new_dataframe['TransactionMonth'] = new_dataframe['TransactionStartTime'].dt.month
    new_dataframe['TransactionYear'] = new_dataframe['TransactionStartTime'].dt.year
    return new_dataframe