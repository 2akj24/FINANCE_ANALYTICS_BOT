# 📊 Financial Growth Chatbot

This **Financial Growth Chatbot** is a Python-based application that provides interactive access to financial data for major tech companies like **Apple**, **Tesla**, and **Microsoft**. It allows users to query revenue, income, assets, liabilities, and cash flow across multiple years using **natural language questions**.

---


## 📦 Dependencies

- Python 3.6+
- pandas
- Standard Python libraries (`os`, `re`, `difflib`, etc.)

---

## 👨‍💻 Author Note

> This was my **first ever project**. Some basic features may be missing, which I will be improving in future updates.  
> I have taken help from **Python Documentation**, **YouTube**, **Forage**, **ChatGPT**, **DeepSeek** and **Other websites**.  
> The financial data is based on analysis of **10-K documents** submitted by these companies over the past 3 years. 😊

---

## 🚀 Future Goals

1. **GUI**: Add a user-friendly graphical interface and package the project as a standalone `.exe` application. - DONE✅
2. **Custom Files**: Allow users to upload their own CSV files in the expected format and analyze various datasets dynamically.

---

## 🗂️ Modules

### 1. Main Modules
- `chatbot.py`: Main application file containing the entire logic
- `Enhanced_Company_Growth_Data.csv`: Primary data source with financial metrics

### 2. Supporting Functions (Integrated in `chatbot.py`)
- `get_trend()`: Calculates growth trends
- `generate_summary()`: Natural language financial summaries
- `parse_question()`: Interprets user questions
- `get_closest_metric()`: Uses fuzzy matching to identify metrics
- `export_company_report()`: Generates text file reports
- `compare_companies()`: Compares financial metrics across companies

---

## 🧠 Supported Question Types

### 1. Basic Queries
- "What is Apple's total revenue in 2024?"
- "Microsoft cash flow 2023"
- "Show Tesla net income"
- "Apple total liabilities all years"

### 2. Trend Analysis
- "How has Microsoft's revenue changed?"
- "Show Tesla cash flow growth"

### 3. Company Comparisons
- "Compare Apple and Tesla net income in 2024"
- "Microsoft vs Apple total assets 2023"

### 4. Data Export
- "Export Apple report"
- "Create Microsoft financial report"

### 5. Full Data Display
- "Show all data for Tesla"
- "Display Microsoft complete financials"

---

## ⚠️ Limitations

- **Data**: Uses fixed datasets (not real-time or dynamic)
- **NLP**: Limited natural language processing capabilities
- **Comparison**: Only supports two-way comparison (not three or more)
- **Export**: No PDF/Excel export options (currently supports only `.txt`)
- **Memory**: No context memory between questions

> ❗ These are on my to-do list for improvement.


---

## 📄 License

**Open-source** – Free to use, modify, and distribute.

---

## 📝 Note

This chatbot is designed as a fully **integrated** Python application. All helper functions are embedded within the main script to eliminate external dependencies. You can extend its functionality by adding new columns to the CSV file or enhancing the parsing logic for better natural language understanding.

##Author: Abhinav Kumar Jha
