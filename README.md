# Vanna AI Demo

A simple demonstration of [Vanna AI](https://vanna.ai/) - AI-powered SQL generation using Google Gemini, PostgreSQL, and ChromaDB.

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start PostgreSQL**:
   ```bash
   cd docker && ./run.sh
   ```

3. **Open the notebook**:
   ```bash
   jupyter notebook notebooks/vanna-ai-demo.ipynb
   ```

**That's it!** The notebook has everything configured:
- ✅ API keys built-in
- ✅ Database settings ready
- ✅ Just run the cells in order

## 📊 What You'll Get

- **Stocks Dataset**: 26,566 historical stock records
- **AI SQL Generation**: Ask questions in natural language
- **Web Interface**: Interactive Flask app at http://localhost:8084

## 🎯 Example Questions

- "What is the average price of GOOGL stock?"
- "Show me the highest volume trading days"
- "Which stocks had the biggest price changes?"

## 🔄 Switch Datasets

To use movies data instead of stocks:
```bash
python3 switch_dataset.py movies
```

## 📁 Project Structure

```
vanna-ai-demo/
├── notebooks/vanna-ai-demo.ipynb  # Main demo notebook
├── docker/                        # PostgreSQL setup
├── data/                          # Sample datasets
└── requirements.txt               # Dependencies
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.