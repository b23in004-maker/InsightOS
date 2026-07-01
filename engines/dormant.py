def analyze_dormant(df):

    dormant_columns = []

    total_rows = len(df)

    for column in df.columns:

        missing = df[column].isnull().sum()

        missing_percent = (missing / total_rows) * 100

        unique = df[column].nunique(dropna=True)

        reason = None

        if missing_percent >= 80:

            reason = "Mostly Missing"

        elif unique <= 1:

            reason = "Constant Value"

        if reason:

            dormant_columns.append({

                "column": column,

                "reason": reason,

                "missing_percent": round(missing_percent,2),

                "unique": unique

            })

    return dormant_columns