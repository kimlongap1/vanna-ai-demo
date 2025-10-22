# Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start PostgreSQL
```bash
cd docker
./run.sh
# Wait for "Database is ready!" message
```

### 3. Open the Notebook
```bash
jupyter notebook notebooks/vanna-ai-demo.ipynb
```

**That's it!** The notebook has everything configured:
- ✅ API keys built-in
- ✅ Database settings ready
- ✅ Just run the cells in order

## 📊 Sample Questions to Try

### Stocks Dataset (Default)
- "What's the average price of GOOGL?"
- "Show me the highest volume trading days"
- "Which stocks had the biggest price swings?"

### Movies Dataset
To switch to movies data:
```bash
python3 switch_dataset.py movies
```

Then try:
- "What are the top 10 highest rated movies?"
- "Show me movies released in 2020"
- "Which movies have the highest vote count?"

## 🌐 Web Interface

In the notebook, run the Flask app cell to get the web interface at http://localhost:8084

## 🔧 Troubleshooting

### Common Issues
1. **Database Connection**: Ensure PostgreSQL is running (`cd docker && ./run.sh`)
2. **Module Errors**: Run `pip install -r requirements.txt`
3. **Port Conflicts**: If port 5433 is busy, the Docker container will fail to start

### Need Help?
- Check the full README.md
- Review the notebook troubleshooting section
- Open an issue in the repository

Happy coding! 🎉