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

<!-- Add demo screenshots here -->
<!-- ![Demo Screenshot](img/demo-screenshot.png) -->
<!-- ![Web Interface](img/web-interface.png) -->

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

1. **ChromaDB OperationalError**
   ```
   OperationalError: Failed to connect to ChromaDB server
   ```
   **Solution**: The notebook is now configured to use a local ChromaDB instance. If you still get this error:
   - Restart the Jupyter kernel
   - Run the cells in order again
   - The ChromaDB data will be stored in `./chromadb_data/`

2. **Port 5433 already in use**
   ```bash
   # Stop any existing PostgreSQL containers
   docker stop $(docker ps -q --filter ancestor=postgres)
   ```

3. **Module not found errors**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

4. **Database connection failed**
   ```bash
   # Check if Docker is running
   docker ps
   
   # Restart the database
   cd docker && ./run.sh
   ```

5. **ChromaDB telemetry warnings**
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
├── img/                        # Images and media for README
├── README.md                   # This file
├── QUICKSTART.md              # Quick start guide
├── requirements.txt           # Python dependencies
└── switch_dataset.py          # Dataset switcher
```


## 🛠️ Tech Stack

This demo showcases a specific tech stack, but Vanna AI supports many alternatives:

### Current Implementation

| Component | Technology | Purpose |
|-----------|------------|---------|
| **LLM** | Google Gemini Pro | AI-powered SQL generation |
| **Database** | PostgreSQL | Sample data storage and query execution |
| **Vector Store** | ChromaDB | Training data storage and retrieval |
| **Web Interface** | Flask | Interactive demo interface |
| **Containerization** | Docker | Easy database setup |

### Vanna AI Flexibility

**🤖 Supported LLMs:**
- Google Gemini (used in this demo)
- OpenAI GPT-3.5/4
- Anthropic Claude
- Azure OpenAI
- Cohere
- Ollama (local models)
- And many more...

**🗄️ Supported Databases:**
- PostgreSQL (used in this demo)
- MySQL
- SQL Server
- BigQuery
- Snowflake
- SQLite
- Oracle
- And many more...

**📊 Supported Vector Stores:**
- ChromaDB (used in this demo)
- Pinecone
- Weaviate
- Qdrant
- Milvus
- FAISS
- And many more...

### Why This Stack?

**Google Gemini**: Excellent SQL generation capabilities with competitive pricing
**PostgreSQL**: Robust, feature-rich database with excellent SQL support
**ChromaDB**: Lightweight, local vector store perfect for demos
**Docker**: Ensures consistent setup across different environments

### Customizing Your Stack

To use different components, simply modify the notebook configuration:

```python
# Example: Switch to OpenAI
from vanna.openai import OpenAI_Chat
vn = OpenAI_Chat(api_key="your-openai-key")

# Example: Switch to MySQL
vn.connect_to_mysql(host='localhost', user='root', password='password', database='mydb')

# Example: Switch to Pinecone
from vanna.pinecone import Pinecone_VectorStore
vn = Pinecone_VectorStore(api_key="your-pinecone-key")
```

## 🎮 How It Works

1. **Database Connection**: Connects to PostgreSQL with sample data
2. **Schema Learning**: AI analyzes your database structure
3. **Training**: Learns from DDL statements and examples
4. **Query Generation**: Converts natural language to SQL using Gemini
5. **Execution**: Runs queries and returns results
6. **Vector Storage**: Stores training data in ChromaDB for future reference

## 🧠 Training Vanna AI

Before you can ask questions, Vanna AI needs to be trained on your database. The notebook includes comprehensive training examples:

### 1. Schema Training (Automatic)

The notebook automatically trains on your database schema:

```python
# Get database schema information
df_information_schema = vn.run_sql("SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_schema = 'public'")

# Generate training plan
plan = vn.get_training_plan_generic(df_information_schema)

# Train on the schema
vn.train(plan=plan)
```

### 2. DDL Training (Table Structure)

Teach Vanna about your table structure:

```python
# DDL statements are powerful because they specify table names, column names, types, and relationships
vn.train(ddl="""
CREATE TABLE stocks (
    date TIMESTAMPTZ NULL,
    symbol TEXT NULL,
    open DOUBLE PRECISION NULL,
    high DOUBLE PRECISION NULL,
    low DOUBLE PRECISION NULL,
    close DOUBLE PRECISION NULL,
    adj_close DOUBLE PRECISION NULL,
    volume BIGINT NULL
)
""")
```

### 3. Documentation Training (Business Context)

Provide business context and domain knowledge:

```python
# Documentation Training
vn.train(documentation="""
Stock market data includes daily trading information with opening, high, low, and closing prices.
Volume represents the number of shares traded. Adjusted close accounts for stock splits and dividends.
Daily range is calculated as high minus low. Price movement is close minus open.
""")
```

### 4. SQL Examples Training

Show Vanna example queries for common patterns:

```python
# SQL Training Examples
vn.train(sql="SELECT symbol, date, close FROM stocks WHERE symbol = 'AAPL' ORDER BY date DESC LIMIT 10")
vn.train(sql="SELECT symbol, AVG(close) as avg_price FROM stocks GROUP BY symbol ORDER BY avg_price DESC")
```

### 5. Training for Movies Dataset

If you switch to movies dataset, use these examples:

```python
# Movies DDL Training
vn.train(ddl="""
CREATE TABLE movies (
    id INTEGER,
    title TEXT,
    vote_average DOUBLE PRECISION,
    vote_count INTEGER,
    release_date DATE,
    genre_ids TEXT
)
""")

# Movies Documentation
vn.train(documentation="""
Movies table contains film data with ratings, genres, and release dates.
Vote average is the average rating (0-10 scale). Vote count is number of ratings.
Genre IDs represent movie categories like action, comedy, drama.
""")

# Movies SQL Examples
vn.train(sql="SELECT title, vote_average FROM movies WHERE vote_average > 8.0 ORDER BY vote_average DESC")
vn.train(sql="SELECT COUNT(*) as movie_count FROM movies WHERE release_date >= '2020-01-01'")
```

### Training Tips

- **Run training once**: Don't retrain unless you add new data
- **Use descriptive documentation**: Explain business context and relationships
- **Provide diverse examples**: Include different query patterns
- **Test after training**: Ask sample questions to verify training worked

### Verify Training Worked

After training, test with these questions:

```python
# Test questions to verify training
question = "What is the average price of GOOGL stock?"
sql = vn.generate_sql(question=question)
print(f"Question: {question}")
print(f"Generated SQL: {sql}")

# Execute and see results
df = vn.run_sql(sql=sql)
print(df)
```

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
