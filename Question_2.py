import pandas as pd

df = pd.read_csv("titles.csv")


def count_vowels(df: pd.DataFrame, column_name: str) -> pd.Series:
    """
    Returns a pandas Series containing the count of vowels in each string of the specified column.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column in which to count the vowels.

    Returns:
    pd.Series: A pandas Series containing the count of vowels in each string of the specified column.
    """
    vowels = set("aeiouAEIOU")
    return df[column_name].str.count("[{}]".format("".join(vowels)))


print(count_vowels(df, "title"))
