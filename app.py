from dotenv import load_dotenv
import os
import importlib

API_backend = importlib.import_module("API-backend")

load_dotenv("locales.env")

app = API_backend.app

app.run(host="10.10.9.102",port=str(os.getenv("port", default="3000")))
