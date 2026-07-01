BUSINESS_TEMPLATES = {

    "customer": [

        "customer_id",
        "name",
        "email",
        "phone",
        "age",
        "gender",
        "city",
        "state",
        "country"

    ],

    "sales": [

        "order_id",
        "customer_id",
        "product_id",
        "quantity",
        "price",
        "discount",
        "sales_date"

    ],

    "employee": [

        "employee_id",
        "employee_name",
        "department",
        "salary",
        "designation",
        "joining_date"

    ]

}


def detect_dataset_type(columns):

    columns = [c.lower() for c in columns]

    if "customer_id" in columns:
        return "customer"

    if "order_id" in columns:
        return "sales"

    if "employee_id" in columns:
        return "employee"

    return None


def analyze_gap(df):

    columns = [c.lower() for c in df.columns]

    dataset_type = detect_dataset_type(columns)

    if dataset_type is None:

        return {

            "dataset_type": "Unknown",

            "missing_columns": [],

            "recommendations": []

        }

    expected = BUSINESS_TEMPLATES[dataset_type]

    missing = []

    recommendations = []

    for column in expected:

        if column not in columns:

            missing.append(column)

            recommendations.append(

                f"Consider adding '{column}' for better business analysis."

            )

    return {

        "dataset_type": dataset_type.title(),

        "missing_columns": missing,

        "recommendations": recommendations

    }