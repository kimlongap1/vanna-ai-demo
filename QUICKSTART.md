# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Setup Environment
```bash
# Run the setup script
./setup.sh

# Edit your API key
cp env.example .env
# Add your Google Gemini API key to .env
```

### 2. Start PostgreSQL
```bash
cd docker
./run.sh
# Wait for "Database is ready!" message
```

### 3. Launch Demo
```bash
# Start Jupyter
jupyter notebook notebooks/

# Open vanna-ai-demo.ipynb
# Run all cells to see the magic! ✨
```

### 4. Web Interface
```python
# In the notebook, run the Flask app cell
from vanna.flask import VannaFlaskApp
app = VannaFlaskApp(vn, allow_llm_to_see_data=True)
app.run()

# Visit http://localhost:8084
```

## 📊 Sample Questions to Try

### Movies Dataset
- "What are the top 10 highest rated movies?"
- "Show me movies released in 2020"
- "Which movies have the highest vote count?"

### Stocks Dataset  
- "What's the average price of AAPL?"
- "Show me the highest volume trading days"
- "Which stocks had the biggest price swings?"

## 🔧 Troubleshooting

### Common Issues
1. **API Key Error**: Make sure GEMINI_API_KEY is set in .env
2. **Database Connection**: Ensure PostgreSQL is running (`cd docker && ./run.sh`)
3. **Module Errors**: Run `pip install -r requirements.txt`

### Need Help?
- Check the full README.md
- Review the notebook troubleshooting section
- Open an issue in the repository

Happy coding! 🎉
