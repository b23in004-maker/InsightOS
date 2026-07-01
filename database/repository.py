from database.db import get_connection


def save_dataset(dataset):

    connection = get_connection()

    cursor = connection.cursor()

    sql = """

    INSERT INTO datasets(

        dataset_name,

        rows_count,

        columns_count,

        quality_score,

        missing_values,

        duplicate_rows

    )

    VALUES(%s,%s,%s,%s,%s,%s)

    """

    values = (

        dataset["dataset_name"],

        dataset["rows"],

        dataset["columns"],

        dataset["quality_score"],

        dataset["missing_values"],

        dataset["duplicate_rows"]

    )

    cursor.execute(sql, values)

    connection.commit()

    cursor.close()

    connection.close()