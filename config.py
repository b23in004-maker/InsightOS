import os

class Config:

    SECRET_KEY = "insightos@2026"

    UPLOAD_FOLDER = "uploads"

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = {"csv"}

    DEBUG = True