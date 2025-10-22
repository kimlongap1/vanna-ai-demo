# Vanna AI Demo Project

A comprehensive demonstration of [Vanna AI](https://vanna.ai/) - an AI-powered SQL generation tool using Google Gemini, PostgreSQL, and ChromaDB.

## 🚀 Quick Start

**Simple! No .env files needed - all configuration is directly in the notebook:**

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start PostgreSQL
cd docker && ./run.sh

# 3. Open the notebook
jupyter notebook notebooks/vanna-ai-demo.ipynb
```

**That's it!** The notebook has all configuration built-in:
- ✅ API keys directly in the code
- ✅ Database settings pre-configured  
- ✅ No environment variables needed
- ✅ Just open and run!

**Alternative: Use the Python script** for automated testing:
```bash
python3 vanna_demo_simple.py
```

## 🚀 Features

- **AI-Powered SQL Generation**: Generate SQL queries from natural language using Google Gemini
- **PostgreSQL Integration**: Connect to PostgreSQL databases with sample data
- **ChromaDB Vector Store**: Store and retrieve training data locally
- **Web Interface**: Interactive Flask-based web UI for SQL generation
- **Sample Datasets**: Pre-loaded with movies and stocks data
- **Docker Support**: Easy setup with Docker containers

## 📋 Prerequisites

- Python 3.9+
- Docker and Docker Compose
- Google Gemini API Key

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd vanna-ai-demo
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env and add your Google Gemini API key
   ```
   
   **Note**: The project now uses environment variables instead of hardcoded values. All configuration is managed through the `.env` file.

4. **Start PostgreSQL with sample data**:
   ```bash
   cd docker
   ./run.sh
   ```
   
   **Note**: By default, the project loads the **stocks** dataset. To switch to movies:
   ```bash
   python3 switch_dataset.py movies
   ```

5. **Test your setup**:
   ```bash
   python3 test_config.py
   ```
   
   This will verify that all environment variables are loaded correctly and the database connection works.

## 🎯 Quick Start

1. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook notebooks/
   ```

2. **Open the demo notebook**:
   - `vanna-ai-demo.ipynb` - Complete demonstration

3. **Run the Flask web interface**:
   ```python
   from vanna.flask import VannaFlaskApp
   app = VannaFlaskApp(vn, allow_llm_to_see_data=True)
   app.run()
   ```

## 📊 Sample Data

The project includes two datasets that you can switch between:

### Movies Dataset
- **Movies**: 4,808 movie records with ratings, genres, and metadata
- **Credits**: 4,805 credit records with cast and crew information

### Stocks Dataset  
- **Stocks**: 26,566 historical stock records with OHLCV (Open, High, Low, Close, Volume)

### Dataset Switching
You can easily switch between datasets using the provided script:

```bash
# Switch to movies dataset
python3 switch_dataset.py movies

# Switch to stocks dataset  
python3 switch_dataset.py stocks

# Check current status
python3 switch_dataset.py status
```

**Note**: Switching datasets will rebuild the Docker container with the new data.

## 🔧 Configuration

### Environment Variables
Create a `.env` file with:
```env
GEMINI_API_KEY=your_gemini_api_key_here
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
```

### Model Configuration
The project uses Google Gemini with the following settings:
- Model: `gemini-pro-latest`
- Vector Store: ChromaDB (local)
- Database: PostgreSQL
- Summarization: Enabled (`allow_llm_to_see_data=True`)

## 📁 Project Structure

```
vanna-ai-demo/
├── data/                   # Sample data files
├── docker/                 # PostgreSQL Docker setup
│   ├── movies/            # Movies dataset
│   ├── stocks/            # Stocks dataset
│   └── *.sh              # Setup scripts
├── notebooks/             # Jupyter notebooks
│   └── vanna-ai-demo.ipynb
├── src/                   # Source code
├── docs/                  # Documentation
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
└── README.md             # This file
```

## 🎮 Usage Examples

### Basic SQL Generation
```python
# Ask questions in natural language
vn.ask("What are the top 10 highest rated movies?")
vn.ask("Show me the average stock price for AAPL over the last month")
```

### Training the Model
```python
# Add DDL statements
vn.train(ddl="CREATE TABLE movies (id INT, title TEXT, rating FLOAT)")

# Add documentation
vn.train(documentation="Movies table contains film data with ratings")

# Add SQL examples
vn.train(sql="SELECT * FROM movies WHERE rating > 8.0")
```

### Web Interface
Access the interactive web interface at `http://localhost:8084` after running:
```python
app = VannaFlaskApp(vn, allow_llm_to_see_data=True)
app.run()
```

## 🔍 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'vertexai'**
   ```bash
   pip install google-cloud-aiplatform
   ```

2. **404 models/gemini-1.5-pro is not found**
   - The model name has been updated to `gemini-pro-latest`
   - Check the notebook configuration

3. **ChromaDB telemetry errors**
   - These are harmless warnings that don't affect functionality
   - They are suppressed in the notebook

### Getting Help

- Check the [Vanna AI Documentation](https://vanna.ai/docs/)
- Review the troubleshooting section in the notebook
- Open an issue in this repository

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Vanna AI](https://vanna.ai/) for the amazing SQL generation framework
- [Google Gemini](https://ai.google.dev/) for the LLM capabilities
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [PostgreSQL](https://www.postgresql.org/) for the database engine
