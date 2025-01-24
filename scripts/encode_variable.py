from sklearn.preprocessing import OneHotEncoder
import pandas as pd


def encodingCategoricalVariables(new_dataframe):
    """
        Encodes categorical variables using OneHotEncoding.

        Parameters:
            new_dataframe (pd.DataFrame): Dataset containing categorical columns.

        Returns:
            pd.DataFrame: Dataset with encoded categorical variables.
        """
    categorical_columns = ['CurrencyCode', 'ProductCategory']
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded_data = encoder.fit_transform(new_dataframe[categorical_columns])
    encoded_new_dataframe = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_columns))
    new_dataframe_encoded = pd.concat([new_dataframe.reset_index(drop=True), encoded_new_dataframe], axis=1)
    new_dataframe_encoded.drop(columns=categorical_columns, inplace=True)
    return new_dataframe_encoded