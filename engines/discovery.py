import pandas as pd


def classify_column(column_name, dtype, unique_count):

    name = column_name.lower()

    if "id" in name:
        return "Identifier"

    if "date" in name or "time" in name:
        return "Date"

    if dtype == "object":
        return "Categorical"

    if "int" in dtype or "float" in dtype:

        if unique_count > 20:
            return "Measure"

        return "Numeric"

    return "Unknown"


def analyze_dataset(df):

    discovery = []

    total_rows = len(df)

    for column in df.columns:

        dtype = str(df[column].dtype)

        unique = int(df[column].nunique())

        missing = int(df[column].isnull().sum())

        completeness = round(
            ((total_rows - missing) / total_rows) * 100,
            2
        )

        discovery.append({

            "column": column,

            "datatype": dtype,

            "classification": classify_column(
                column,
                dtype,
                unique
            ),

            "unique": unique,

            "missing": missing,

            "completeness": completeness

        })

    return discovery