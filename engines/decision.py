def generate_decision_report(dataset):
    """
    Generates an overall health score and business recommendations
    based on the analyzed dataset.
    """

    recommendations = []

    quality_score = dataset.get("quality_score", 0)
    missing_values = dataset.get("missing_values", 0)
    duplicate_rows = dataset.get("duplicate_rows", 0)
    dormant = dataset.get("dormant", [])
    gap = dataset.get("gap", {})

    # -------------------------------
    # Dataset Health
    # -------------------------------

    if quality_score >= 95:
        health = "Excellent 🟢"

    elif quality_score >= 85:
        health = "Good 🟢"

    elif quality_score >= 70:
        health = "Fair 🟡"

    else:
        health = "Poor 🔴"

    # -------------------------------
    # Recommendations
    # -------------------------------

    if missing_values > 0:
        recommendations.append(
            f"Dataset contains {missing_values} missing values. Consider cleaning or imputing the missing data."
        )

    if duplicate_rows > 0:
        recommendations.append(
            f"Dataset contains {duplicate_rows} duplicate rows. Remove duplicates to improve data quality."
        )

    if dormant:
        recommendations.append(
            f"{len(dormant)} dormant column(s) detected. Review and archive unused attributes."
        )

    missing_columns = gap.get("missing_columns", [])

    if missing_columns:
        recommendations.append(
            "Important business attributes are missing: "
            + ", ".join(missing_columns)
            + "."
        )

    if not recommendations:
        recommendations.append(
            "Excellent! No major data quality issues were detected."
        )

    # -------------------------------
    # Return Report
    # -------------------------------

    return {
        "health": health,
        "score": quality_score,
        "recommendations": recommendations
    }