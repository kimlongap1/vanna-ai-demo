#!/bin/bash

# Vanna AI Demo Setup Script
# This script sets up the complete demo environment

set -e

echo "🚀 Setting up Vanna AI Demo Project..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not installed."
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "⚠️  Please edit .env file and add your Google Gemini API key"
fi

# Create ChromaDB data directory
echo "📁 Creating ChromaDB data directory..."
mkdir -p chromadb_data

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker is not installed. You'll need to install it to run PostgreSQL."
    echo "   Visit: https://docs.docker.com/get-docker/"
else
    echo "🐳 Docker is available. You can start PostgreSQL with:"
    echo "   cd docker && ./run.sh"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your Google Gemini API key"
echo "2. Start PostgreSQL: cd docker && ./run.sh"
echo "3. Launch Jupyter: jupyter notebook notebooks/"
echo "4. Open vanna-ai-demo.ipynb"
echo ""
echo "Happy coding! 🎉"
