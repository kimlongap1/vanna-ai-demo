# Vanna AI Demo

A simple demonstration of [Vanna AI](https://vanna.ai/) - AI-powered SQL generation using Google Gemini, PostgreSQL, and ChromaDB.

## 🚀 Quick Start

### Prerequisites

Before you begin, make sure you have:

- **Python 3.9+** installed on your system
- **Docker** installed and running
- **Google Gemini API Key** (get one from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Step-by-Step Setup

#### 1. Clone and Install Dependencies

```bash
# Clone the repository
git clone https://github.com/kimlongap1/vanna-ai-demo.git
cd vanna-ai-demo

# Install Python dependencies
pip install -r requirements.txt
```

#### 2. Start PostgreSQL Database

```bash
# Navigate to docker directory
cd docker

# Build and start PostgreSQL with sample data
./run.sh

# Wait for "Database is ready!" message
# The database will be available on localhost:5433
```

**What happens here:**
- Builds a PostgreSQL Docker container
- Loads sample stocks data (26,566 records)
- Database runs on port 5433 (to avoid conflicts)
- Credentials: `postgres:password@localhost:5433/postgres`

#### 3. Launch the Demo

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/vanna-ai-demo.ipynb

# Or if you prefer JupyterLab
jupyter lab notebooks/vanna-ai-demo.ipynb
```

#### 4. Run the Notebook

1. **Open the notebook** in your browser
2. **Run all cells** in order (Shift+Enter)
3. **Wait for training** - the AI will learn your database schema
4. **Try sample questions** like "What is the average price of GOOGL stock?"

**That's it!** The notebook has everything configured:
- ✅ API keys built-in
- ✅ Database settings ready
- ✅ No environment variables needed
- ✅ Just run the cells in order

## 📊 What You'll Get

### Sample Data
- **Stocks Dataset**: 26,566 historical stock records with OHLCV data
- **Movies Dataset**: 4,808 movie records with ratings and metadata (optional)

### Features
- **AI SQL Generation**: Ask questions in natural language
- **Web Interface**: Interactive Flask app at http://localhost:8084
- **Real-time Training**: AI learns from your database schema
- **Multiple Datasets**: Switch between stocks and movies data

## 🎯 Example Questions to Try

### Stocks Dataset (Default)
- "What's the average price of GOOGL?"
- "Show me the highest volume trading days"
- "Which stocks had the biggest price swings?"
- "What was AAPL's highest closing price?"
- "Find stocks with volume above 10 million"

### Movies Dataset
To switch to movies data:
```bash
python3 switch_dataset.py movies
```

Then try:
- "What are the top 10 highest rated movies?"
- "Show me movies released in 2020"
- "Which movies have the highest vote count?"
- "Find action movies with ratings above 8.0"

## 🔄 Switch Datasets

The project includes two sample datasets. Switch between them easily:

```bash
# Switch to movies dataset
python3 switch_dataset.py movies

# Switch back to stocks dataset  
python3 switch_dataset.py stocks

# Check current dataset
python3 switch_dataset.py status
```

**Note**: Switching datasets will rebuild the Docker container with new data.

## 🌐 Web Interface

After running the notebook, you can also use the web interface:

1. **Run the Flask app cell** in the notebook
2. **Visit** http://localhost:8084
3. **Ask questions** in the web interface
4. **View generated SQL** and results

## 🔧 Troubleshooting

### Common Issues

1. **Port 5433 already in use**
   ```bash
   # Stop any existing PostgreSQL containers
   docker stop $(docker ps -q --filter ancestor=postgres)
   ```

2. **Module not found errors**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

3. **Database connection failed**
   ```bash
   # Check if Docker is running
   docker ps
   
   # Restart the database
   cd docker && ./run.sh
   ```

4. **ChromaDB telemetry warnings**
   - These are harmless and don't affect functionality
   - They're automatically suppressed in the notebook

### Getting Help

- Check the [Vanna AI Documentation](https://vanna.ai/docs/)
- Review the troubleshooting section in the notebook
- Open an issue in this repository

## 📁 Project Structure

```
vanna-ai-demo/
├── notebooks/
│   └── vanna-ai-demo.ipynb    # Main demo notebook
├── docker/                     # PostgreSQL setup
│   ├── movies/                # Movies dataset
│   ├── stocks/                # Stocks dataset
│   └── *.sh                   # Setup scripts
├── data/                       # Sample datasets
├── docs/                       # Documentation
├── README.md                   # This file
├── QUICKSTART.md              # Quick start guide
├── requirements.txt           # Python dependencies
└── switch_dataset.py          # Dataset switcher
```

## 🎮 How It Works

1. **Database Connection**: Connects to PostgreSQL with sample data
2. **Schema Learning**: AI analyzes your database structure
3. **Training**: Learns from DDL statements and examples
4. **Query Generation**: Converts natural language to SQL
5. **Execution**: Runs queries and returns results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Vanna AI](https://vanna.ai/) for the amazing SQL generation framework
- [Google Gemini](https://ai.google.dev/) for the LLM capabilities
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [PostgreSQL](https://www.postgresql.org/) for the database engine