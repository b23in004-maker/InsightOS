from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    flash
)

from werkzeug.utils import secure_filename
import pandas as pd
import os

from config import Config
from etl import process_dataset

from catalog.catalog import add_dataset, get_catalog
from database.repository import save_dataset
from reports.generator import generate_pdf


app = Flask(__name__)
app.config.from_object(Config)

# Required for flash messages
app.secret_key = app.config.get("SECRET_KEY", "insightos_secret_key")

# Stores the latest uploaded dataset
dashboard_data = None


# ============================================
# Check Allowed File Extensions
# ============================================

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    )


# ============================================
# HOME
# ============================================

@app.route("/")
def home():
    return render_template("home.html")


# ============================================
# ABOUT
# ============================================

@app.route("/about")
def about():
    return render_template("about.html")


# ============================================
# FEATURES
# ============================================

@app.route("/features")
def features():
    return render_template("features.html")


# ============================================
# CONTACT
# ============================================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ============================================
# UPLOAD DATASET
# ============================================

@app.route("/upload", methods=["GET", "POST"])
def upload():

    global dashboard_data

    if request.method == "POST":

        if "file" not in request.files:
            return render_template(
                "upload.html",
                error="No file was selected."
            )

        file = request.files["file"]

        if file.filename == "":
            return render_template(
                "upload.html",
                error="Please select a CSV file."
            )

        if not allowed_file(file.filename):
            return render_template(
                "upload.html",
                error="Only CSV files are allowed."
            )

        try:

            filename = secure_filename(file.filename)

            os.makedirs(
                app.config["UPLOAD_FOLDER"],
                exist_ok=True
            )

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(filepath)

            # Process Dataset
            dashboard_data = process_dataset(filepath)

            # Save to SQLite
            save_dataset(dashboard_data)

            # Save to Metadata Catalog
            add_dataset(dashboard_data)

            flash(
                "Dataset uploaded successfully!",
                "success"
            )

            return redirect(url_for("dashboard"))

        except pd.errors.EmptyDataError:

            return render_template(
                "upload.html",
                error="The uploaded CSV file is empty."
            )

        except pd.errors.ParserError:

            return render_template(
                "upload.html",
                error="The uploaded CSV file is corrupted or has an invalid format."
            )

        except Exception as e:

            return render_template(
                "upload.html",
                error=f"Unexpected Error: {str(e)}"
            )

    return render_template("upload.html")


# ============================================
# DASHBOARD
# ============================================

@app.route("/dashboard")
def dashboard():

    global dashboard_data

    return render_template(
        "dashboard.html",
        data=dashboard_data
    )


# ============================================
# METADATA CATALOG
# ============================================

@app.route("/catalog")
def catalog():

    datasets = get_catalog()

    return render_template(
        "catalog.html",
        datasets=datasets
    )


# ============================================
# DOWNLOAD PDF REPORT
# ============================================

@app.route("/download-report")
def download_report():

    global dashboard_data

    if dashboard_data is None:

        flash(
            "Please upload a dataset before downloading the report.",
            "warning"
        )

        return redirect(url_for("upload"))

    pdf = generate_pdf(dashboard_data)

    return send_file(
        pdf,
        as_attachment=True,
        download_name="InsightOS_Report.pdf"
    )


# ============================================
# CUSTOM ERROR PAGES
# ============================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):

    return render_template("500.html"), 500


# ============================================
# RUN APPLICATION
# ============================================

if __name__ == "__main__":

    os.makedirs(
        app.config["UPLOAD_FOLDER"],
        exist_ok=True
    )

    app.run(
        debug=app.config["DEBUG"]
    )