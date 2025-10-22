"""
Vanna AI Setup Module

This module provides a pre-configured Vanna instance with Google Gemini and ChromaDB.
"""

import os
import sys
import warnings
from io import StringIO

from vanna.chromadb import ChromaDB_VectorStore
from vanna.google import GoogleGeminiChat
from .config import config

# Suppress warnings
warnings.filterwarnings('ignore', category=UserWarning, module='tqdm')

class VannaDemo(ChromaDB_VectorStore, GoogleGeminiChat):
    """
    Pre-configured Vanna instance for the demo project.
    
    This class combines ChromaDB for vector storage and Google Gemini for LLM capabilities.
    """
    
    def __init__(self, custom_config=None):
        """
        Initialize the Vanna demo instance.
        
        Args:
            custom_config (dict, optional): Custom configuration to override defaults
        """
        # Validate configuration
        config.validate_config()
        
        # Disable ChromaDB telemetry to avoid errors
        os.environ['ANONYMIZED_TELEMETRY'] = 'False'
        os.environ['GRPC_DNS_RESOLVER'] = 'native'
        os.environ['TOKENIZERS_PARALLELISM'] = 'false'
        
        # Temporarily suppress stderr to hide telemetry errors
        old_stderr = sys.stderr
        sys.stderr = StringIO()
        
        try:
            # Configure ChromaDB with telemetry disabled
            chromadb_config = custom_config or {}
            chromadb_config.setdefault('path', config.VANNA_CHROMADB_PATH)
            
            ChromaDB_VectorStore.__init__(self, config=chromadb_config)
            
            # Configure Google Gemini with proper parameters
            gemini_config = {
                'api_key': config.GEMINI_API_KEY,
                'model_name': config.GEMINI_MODEL,
                'allow_llm_to_see_data': config.VANNA_ALLOW_LLM_TO_SEE_DATA
            }
            
            GoogleGeminiChat.__init__(self, config=gemini_config)
            
        finally:
            # Restore stderr
            sys.stderr = old_stderr
    
    def connect_to_postgres(self):
        """Connect to the PostgreSQL database using configuration settings."""
        self.connect_to_postgres(
            host=config.POSTGRES_HOST,
            dbname=config.POSTGRES_DB,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD,
            port=config.POSTGRES_PORT
        )
    
    def setup_sample_training_data(self):
        """Set up sample training data for movies and stocks datasets."""
        
        # Movies dataset training
        self.train(ddl="""
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            overview TEXT,
            release_date DATE,
            vote_average FLOAT,
            vote_count INTEGER,
            popularity FLOAT,
            genre_ids TEXT,
            original_language TEXT,
            original_title TEXT,
            backdrop_path TEXT,
            poster_path TEXT,
            adult BOOLEAN,
            video BOOLEAN
        )
        """)
        
        self.train(documentation="""
        Movies table contains film data including:
        - Basic info: title, overview, release_date
        - Ratings: vote_average (0-10 scale), vote_count
        - Metadata: popularity, genre_ids, language
        - Media: backdrop_path, poster_path
        """)
        
        # Stocks dataset training
        self.train(ddl="""
        CREATE TABLE stocks (
            date TIMESTAMPTZ,
            symbol TEXT,
            open DOUBLE PRECISION,
            high DOUBLE PRECISION,
            low DOUBLE PRECISION,
            close DOUBLE PRECISION,
            adj_close DOUBLE PRECISION,
            volume BIGINT
        )
        """)
        
        self.train(documentation="""
        Stocks table contains historical stock market data:
        - OHLCV data: open, high, low, close, volume
        - Adjusted close: accounts for splits and dividends
        - Symbol: stock ticker (e.g., AAPL, GOOGL)
        - Date: trading date with timezone
        """)
        
        # Sample SQL queries for training
        sample_queries = [
            "SELECT title, vote_average FROM movies WHERE vote_average > 8.0 ORDER BY vote_average DESC",
            "SELECT symbol, AVG(close) as avg_price FROM stocks GROUP BY symbol ORDER BY avg_price DESC",
            "SELECT COUNT(*) as total_movies FROM movies",
            "SELECT symbol, MAX(high) as highest_price FROM stocks GROUP BY symbol",
            "SELECT title, release_date FROM movies WHERE release_date >= '2020-01-01' ORDER BY release_date DESC"
        ]
        
        for query in sample_queries:
            self.train(sql=query)
        
        print("✅ Sample training data has been added!")
        print("📊 Movies dataset: DDL, documentation, and sample queries")
        print("📈 Stocks dataset: DDL, documentation, and sample queries")

def create_vanna_instance():
    """Create and return a configured Vanna instance."""
    return VannaDemo()

def setup_demo():
    """Complete demo setup including database connection and training data."""
    print("🚀 Setting up Vanna AI Demo...")
    
    # Create Vanna instance
    vn = create_vanna_instance()
    print("✅ Vanna instance created")
    
    # Connect to database
    try:
        vn.connect_to_postgres()
        print("✅ Connected to PostgreSQL")
    except Exception as e:
        print(f"⚠️  Database connection failed: {e}")
        print("💡 Make sure PostgreSQL is running with: cd docker && ./run.sh")
    
    # Set up training data
    vn.setup_sample_training_data()
    
    print("🎉 Demo setup complete!")
    return vn
