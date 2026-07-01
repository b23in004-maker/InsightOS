import json
import os
from datetime import datetime

CATALOG_FILE = "catalog/metadata.json"


def load_catalog():

    if not os.path.exists(CATALOG_FILE):
        return []

    with open(CATALOG_FILE, "r") as f:
        return json.load(f)


def save_catalog(data):

    with open(CATALOG_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_dataset(dataset):

    catalog = load_catalog()

    catalog.append({

        "dataset_name": dataset["dataset_name"],

        "rows": dataset["rows"],

        "columns": dataset["columns"],

        "quality_score": dataset["quality_score"],

        "uploaded_at": datetime.now().strftime("%d-%m-%Y %H:%M")

    })

    save_catalog(catalog)


def get_catalog():

    return load_catalog()