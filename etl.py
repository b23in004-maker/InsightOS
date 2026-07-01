import os
import pandas as pd

from engines.discovery import analyze_dataset
from engines.dormant import analyze_dormant
from engines.gap import analyze_gap
from engines.decision import generate_decision_report


def process_dataset(filepath):

    # =====================================
    # EXTRACT
    # =====================================

    df = pd.read_csv(filepath)

    # =====================================
    # BASIC DATASET STATISTICS
    # =====================================

    rows = df.shape[0]
    columns = df.shape[1]

    missing = int(df.isnull().sum().sum())

    duplicates = int(df.duplicated().sum())

    column_names = list(df.columns)

    memory_usage = round(
        df.memory_usage(deep=True).sum() / 1024,
        2
    )

    # =====================================
    # DATA TYPES
    # =====================================

    data_types = {}

    for column in df.columns:
        data_types[column] = str(df[column].dtype)

    # =====================================
    # MISSING VALUES PER COLUMN
    # =====================================

    missing_per_column = {}

    for column in df.columns:
        missing_per_column[column] = int(df[column].isnull().sum())

    # =====================================
    # QUALITY SCORE
    # =====================================

    total_cells = rows * columns

    if total_cells == 0:
        quality_score = 0
    else:
        quality_score = round(
            ((total_cells - missing) / total_cells) * 100,
            2
        )

    # =====================================
    # DISCOVERY ENGINE
    # =====================================

    discovery = analyze_dataset(df)

    # =====================================
    # DORMANT DATA ENGINE
    # =====================================

    dormant = analyze_dormant(df)

    # =====================================
    # GAP DETECTION ENGINE
    # =====================================

    gap = analyze_gap(df)

    # =====================================
    # DECISION INTELLIGENCE ENGINE
    # =====================================

    decision = generate_decision_report({

        "quality_score": quality_score,

        "missing_values": missing,

        "duplicate_rows": duplicates,

        "dormant": dormant,

        "gap": gap

    })

    # =====================================
    # FINAL DATA OBJECT
    # =====================================

    dataset = {

        "dataset_name": os.path.basename(filepath),

        "rows": rows,

        "columns": columns,

        "missing_values": missing,

        "duplicate_rows": duplicates,

        "column_names": column_names,

        "data_types": data_types,

        "memory_usage": memory_usage,

        "missing_per_column": missing_per_column,

        "quality_score": quality_score,

        "discovery": discovery,

        "dormant": dormant,

        "gap": gap,

        "decision": decision

    }

    return dataset