"""
Vanna AI Demo Configuration Module

This module provides configuration management for the Vanna AI demo project.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for Vanna AI Demo"""
    
    # Google Gemini Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'your_gemini_api_key_here')
    GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-pro-latest')
    
    # PostgreSQL Configuration
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5433")')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'postgres')
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')
    
    # Vanna AI Configuration
    VANNA_ALLOW_LLM_TO_SEE_DATA = os.getenv('VANNA_ALLOW_LLM_TO_SEE_DATA', 'true').lower() == 'true'
    VANNA_CHROMADB_PATH = os.getenv('VANNA_CHROMADB_PATH', './chromadb_data')
    
    # Flask Configuration
    FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    FLASK_PORT = int(os.getenv('FLASK_PORT', '8084'))
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'true').lower() == 'true'
    
    @classmethod
    def get_postgres_connection_string(cls):
        """Get PostgreSQL connection string"""
        return f"postgresql://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}@{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}"
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        if cls.GEMINI_API_KEY == 'your_gemini_api_key_here':
            raise ValueError("Please set your GEMINI_API_KEY in the .env file")
        return True

# Create a global config instance
config = Config()
