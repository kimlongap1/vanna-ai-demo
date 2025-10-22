#!/usr/bin/env python3
"""
Test script to verify environment variable configuration
"""

import sys
import os
sys.path.append('src')

from config import config

def test_configuration():
    """Test that all configuration values are loaded correctly"""
    
    print("🧪 Testing Configuration System")
    print("=" * 50)
    
    # Test Gemini configuration
    print(f"🤖 Gemini API Key: {'✅ Set' if config.GEMINI_API_KEY and config.GEMINI_API_KEY != 'your-gemini-api-key-here' else '❌ Not set'}")
    print(f"🤖 Gemini Model: {config.GEMINI_MODEL}")
    
    # Test PostgreSQL configuration
    print(f"📊 PostgreSQL Host: {config.POSTGRES_HOST}")
    print(f"📊 PostgreSQL Port: {config.POSTGRES_PORT}")
    print(f"📊 PostgreSQL Database: {config.POSTGRES_DB}")
    print(f"📊 PostgreSQL User: {config.POSTGRES_USER}")
    print(f"📊 PostgreSQL Password: {'✅ Set' if config.POSTGRES_PASSWORD else '❌ Not set'}")
    
    # Test validation
    print("\n🔍 Configuration Validation:")
    try:
        config.validate_config()
        print("✅ Configuration validation passed!")
    except Exception as e:
        print(f"❌ Configuration validation failed: {e}")
        return False
    
    # Test database connection
    print("\n🔌 Testing Database Connection:")
    try:
        import psycopg2
        conn = psycopg2.connect(
            host=config.POSTGRES_HOST,
            port=config.POSTGRES_PORT,
            database=config.POSTGRES_DB,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM stocks;")
        count = cursor.fetchone()[0]
        print(f"✅ Database connection successful! Stocks table has {count} records")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False
    
    print("\n🎉 All tests passed! Configuration is working correctly.")
    return True

if __name__ == "__main__":
    success = test_configuration()
    sys.exit(0 if success else 1)
