"""This module is used to retrieve the environment variable from the .env file"""

import os
from dotenv import load_dotenv


class SystemConfig:
    """This class is used to retrieve the environment variable from the .env file"""

    def __init__(self):
        # Load the .env file
        load_dotenv()

    @staticmethod
    def get_pythonpath():
        """Retrieve the value of the variable from the PYTHONPATH"""
        return os.getenv("PYTHONPATH")

    @staticmethod
    def get_openai_api_version():
        """Retrieve the value of the variable from the OPENAI_API_VERSION"""
        return os.getenv("OPENAI_API_VERSION")

    @staticmethod
    def get_openai_img_version():
        """Retrieve the value of the variable from the OPENAI_IMG_VERSION"""
        return os.getenv("OPENAI_IMG_VERSION")

    @staticmethod
    def get_whisper_version():
        """Retrieve the value of the variable from the WHISPER_VERSION"""
        return os.getenv("WHISPER_VERSION")

    @staticmethod
    def get_openai_api_endpoint():
        """Retrieve the value of the variable from the OPENAI_API_ENDPOINT"""
        return os.getenv("OPENAI_API_ENDPOINT")

    @staticmethod
    def get_openai_35_endpoint():
        """Retrieve the value of the variable from the OPENAI_35_ENDPOINT"""
        return os.getenv("OPENAI_35_ENDPOINT")

    @staticmethod
    def get_openai_vision_endpoint():
        """Retrieve the value of the variable from the OPENAI_VISION_ENDPOINT"""
        return os.getenv("OPENAI_VISION_ENDPOINT")

    @staticmethod
    def get_openai_emb_endpoint():
        """Retrieve the value of the variable from the OPENAI_EMB_ENDPOINT"""
        return os.getenv("OPENAI_EMB_ENDPOINT")

    @staticmethod
    def get_openai_img_endpoint():
        """Retrieve the value of the variable from the OPENAI_IMG_ENDPOINT"""
        return os.getenv("OPENAI_IMG_ENDPOINT")

    @staticmethod
    def get_whisper_endpoint():
        """Retrieve the value of the variable from the WHISPER_ENDPOINT"""
        return os.getenv("WHISPER_ENDPOINT")

    @staticmethod
    def get_search_endpoint():
        """Retrieve the value of the variable from the SEARCH_ENDPOINT"""
        return os.getenv("SEARCH_ENDPOINT")

    @staticmethod
    def get_azure_ocr_endpoint():
        """Retrieve the value of the variable from the AZURE_OCR_ENDPOINT"""
        return os.getenv("AZURE_OCR_ENDPOINT")

    @staticmethod
    def get_azure_blob_endpoint():
        """Retrieve the value of the variable from the AZURE_BLOB_ENDPOINT"""
        return os.getenv("AZURE_BLOB_ENDPOINT")

    @staticmethod
    def get_azure_search_endpoint():
        """Retrieve the value of the variable from the AZURE_SEARCH_ENDPOINT"""
        return os.getenv("AZURE_SEARCH_ENDPOINT")

    @staticmethod
    def get_openai_35_engine():
        """Retrieve the value of the variable from the OPENAI_35_ENGINE"""
        return os.getenv("OPENAI_35_ENGINE")

    @staticmethod
    def get_openai_api_engine():
        """Retrieve the value of the variable from the OPENAI_API_ENGINE"""
        return os.getenv("OPENAI_API_ENGINE")

    @staticmethod
    def get_openai_vision_engine():
        """Retrieve the value of the variable from the OPENAI_VISION_ENGINE"""
        return os.getenv("OPENAI_VISION_ENGINE")

    @staticmethod
    def get_openai_emb_engine():
        """Retrieve the value of the variable from the OPENAI_EMB_ENGINE"""
        return os.getenv("OPENAI_EMB_ENGINE")

    @staticmethod
    def get_whisper_engine():
        """Retrieve the value of the variable from the WHISPER_ENGINE"""
        return os.getenv("WHISPER_ENGINE")

    @staticmethod
    def get_azure_bing_endpoint():
        """Retrieve the value of the variable from the Azure_BING_ENDPOINT"""
        return os.getenv("Azure_BING_ENDPOINT")

    @staticmethod
    def get_search_key():
        """Retrieve the value of the variable from the SEARCH_KEY"""
        return os.getenv("SEARCH_KEY")

    @staticmethod
    def get_openai_35_key():
        """Retrieve the value of the variable from the OPENAI_35_KEY"""
        return os.getenv("OPENAI_35_KEY")

    @staticmethod
    def get_openai_api_key():
        """Retrieve the value of the variable from the OPENAI_API_KEY"""
        return os.getenv("OPENAI_API_KEY")

    @staticmethod
    def get_openai_vision_key():
        """Retrieve the value of the variable from the OPENAI_VISION_KEY"""
        return os.getenv("OPENAI_VISION_KEY")

    @staticmethod
    def get_openai_img_key():
        """Retrieve the value of the variable from the OPENAI_IMG_KEY"""
        return os.getenv("OPENAI_IMG_KEY")

    @staticmethod
    def get_openai_emb_key():
        """Retrieve the value of the variable from the OPENAI_EMB_KEY"""
        return os.getenv("OPENAI_EMB_KEY")

    @staticmethod
    def get_whisper_key():
        """Retrieve the value of the variable from the WHISPER_KEY"""
        return os.getenv("WHISPER_KEY")

    @staticmethod
    def get_azure_bing_key():
        """Retrieve the value of the variable from the Azure_BING_KEY"""
        return os.getenv("Azure_BING_KEY")

    @staticmethod
    def get_azure_ocr_key():
        """Retrieve the value of the variable from the AZURE_OCR_KEY"""
        return os.getenv("AZURE_OCR_KEY")

    @staticmethod
    def get_azure_blob_key():
        """Retrieve the value of the variable from the AZURE_BLOB_KEY"""
        return os.getenv("AZURE_BLOB_KEY")

    @staticmethod
    def get_azure_search_key():
        """Retrieve the value of the variable from the AZURE_SEARCH_KEY"""
        return os.getenv("AZURE_SEARCH_KEY")

    @staticmethod
    def get_api_token():
        """Retrieve the value of the variable from the API_TOKEN"""
        return os.getenv("API_TOKEN")

    @staticmethod
    def get_error_msg():
        """Retrieve the value of the variable from the ERROR_MSG"""
        return os.getenv("ERROR_MSG")

    @staticmethod
    def get_google_application_credentials():
        """Retrieve the value of the variable from the GOOGLE_APPLICATION_CREDENTIALS"""
        return os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    @staticmethod
    def get_debug():
        """Retrieve the value of the variable from the DEBUG"""
        return os.getenv("DEBUG")

    @staticmethod
    def get_db_host():
        """Retrieve the value of the variable from the DB_HOST"""
        return os.getenv("DB_HOST")

    @staticmethod
    def get_db_user():
        """Retrieve the value of the variable from the DB_USER"""
        return os.getenv("DB_USER")

    @staticmethod
    def get_db_pass():
        """Retrieve the value of the variable from the DB_PASS"""
        return os.getenv("DB_PASS")

    @staticmethod
    def get_db_name():
        """Retrieve the value of the variable from the DB_NAME"""
        return os.getenv("DB_NAME")

    @staticmethod
    def get_redis_host():
        """Retrieve the value of the variable from the REDIS_HOST"""
        return os.getenv("REDIS_HOST")

    @staticmethod
    def get_google_api_key():
        """Retrieve the value of the variable from the GOOGLE_API_KEY"""
        return os.getenv("GOOGLE_API_KEY")

    @staticmethod
    def get_project_id():
        """Retrieve the value of the variable from the PROJECT_ID"""
        return os.getenv("PROJECT_ID")

    @staticmethod
    def get_processor_id():
        """Retrieve the value of the variable from the PROCESSOR_ID"""
        return os.getenv("PROCESSOR_ID")
