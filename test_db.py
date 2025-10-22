#!/usr/bin/env python3
"""
Database Connection Test Script
Tests the PostgreSQL connection and shows sample data
"""

import psycopg2
import sys

def test_database_connection():
    """Test the database connection and show sample data"""
    
    # Database connection parameters
    conn_params = {
        'host': 'localhost',
        'port': 5433,
        'database': 'postgres',
        'user': 'postgres',
        'password': 'password'
    }
    
    try:
        print("🔌 Testing database connection...")
        
        # Connect to database
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        
        print("✅ Successfully connected to PostgreSQL!")
        
        # Test movies table
        print("\n📊 Testing movies table...")
        cursor.execute("SELECT COUNT(*) FROM movies;")
        movie_count = cursor.fetchone()[0]
        print(f"   Movies in database: {movie_count}")
        
        # Show sample movie
        cursor.execute("SELECT title, vote_average FROM movies ORDER BY vote_average DESC LIMIT 1;")
        best_movie = cursor.fetchone()
        if best_movie:
            print(f"   Highest rated movie: {best_movie[0]} ({best_movie[1]}/10)")
        
        # Test credits table if it exists
        try:
            cursor.execute("SELECT COUNT(*) FROM credits;")
            credit_count = cursor.fetchone()[0]
            print(f"   Credits in database: {credit_count}")
        except psycopg2.Error:
            print("   Credits table not found (this is normal for stocks schema)")
        
        cursor.close()
        conn.close()
        
        print("\n🎉 Database is ready for Vanna AI demo!")
        print("\nConnection string:")
        print(f"postgresql://postgres:password@localhost:5433/postgres")
        
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Database connection failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_database_connection()
    sys.exit(0 if success else 1)