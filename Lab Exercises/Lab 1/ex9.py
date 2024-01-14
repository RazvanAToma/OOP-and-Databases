# Write a Pandas program to detect missing values of a given DataFrame.

import pandas as pd
import numpy as np

dict = {
    'Name': ['Roberto', 'Miguel', 'Julia', 'John', 'Petter'],
    'Age': [45, 24, np.nan, 54, 28],
    'Nationality': ['IT', 'ES', 'GB', 'US', 'NO'],
    'Sex': ['M', 'M', 'F', 'M', 'M']
}
dataframe = pd.DataFrame(data=dict)

print(dataframe)

missing_values_dataframe = dataframe.isnull()

print(missing_values_dataframe)

missing_values_count_dataframe = missing_values_dataframe.sum()

print(missing_values_count_dataframe)



df = pd.DataFrame({
    'Name': ['Roberto', 'Miguel', 'Julia', 'John', 'Petter'],
    'Age': [45, 24, np.nan, 54, 28],
    'Nationality': ['IT', 'ES', 'GB', 'US', 'NO'],
    'Sex': ['M', 'M', 'F', 'M', 'M']},
    index = ['1', '2', '3', '4', '5'],
    columns = ['Name', 'Age', 'Nationality', 'Sex']
)

print(df)

missing_values_df = df.isnull()

print(missing_values_df)

missing_values_count_df = missing_values_df.sum()

print(missing_values_count_df)
