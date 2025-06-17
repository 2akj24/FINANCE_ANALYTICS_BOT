import pandas as pd
import numpy as np

# Load original CSV
df = pd.read_csv("Financials_Microsoft_Tesla_Apple.csv")

# Metrics to compute
metrics = ['Total Revenue', 'Net Income', 'Total Assets', 'Total Liabilities', 'Cash Flow']
all_stats = []

for company in df['Company'].unique():
    data = df[df['Company'] == company].sort_values(by='Year')
    stats = {'Company': company}
    
    for metric in metrics:
        vals = data[metric].values
        if len(vals) == 3:
            stats[f"{metric} 2022"] = vals[0]
            stats[f"{metric} 2023"] = vals[1]
            stats[f"{metric} 2024"] = vals[2]
            stats[f"{metric} Growth 2022-2023 (%)"] = round(((vals[1] - vals[0]) / vals[0]) * 100, 2)
            stats[f"{metric} Growth 2023-2024 (%)"] = round(((vals[2] - vals[1]) / vals[1]) * 100, 2)
            stats[f"{metric} Growth 2022-2024 (%)"] = round(((vals[2] - vals[0]) / vals[0]) * 100, 2)
            stats[f"{metric} Mean"] = round(np.mean(vals), 2)

    all_stats.append(stats)

# Save result
final_df = pd.DataFrame(all_stats)
final_df.to_csv("Enhanced_Company_Growth_Data.csv", index=False)


# Load enhanced data
df = pd.read_csv("Enhanced_Company_Growth_Data.csv")

def ask_bot():
    print("\n📊 Welcome to the Financial Growth Chatbot!")
    print("Ask things like:")
    print(" - 'Tesla 2023 net income'")
    print(" - 'Apple revenue growth 2022-2024'")
    print(" - 'Microsoft average cash flow'")
    print(" - 'Show all data for Tesla'\n")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Ask your question: ").lower()
        if question == 'exit':
            break

        matched = False
        for company in df['Company']:
            if company.lower() in question:
                row = df[df['Company'] == company]

                if "all data" in question:
                    print(f"\n📊 Full financial data for {company}:\n{row.T}\n")
                    matched = True
                    break

                for col in df.columns:
                    if col.lower().replace(" ", "").replace("-", "") in question.replace(" ", "").replace("-", ""):
                        print(f"\n📌 {company} - {col}: {row.iloc[0][col]}\n")
                        matched = True
                        break

                # Try matching on key phrases
                if not matched:
                    for col in df.columns:
                        if any(word in col.lower() for word in question.split()):
                            print(f"\n📌 {company} - {col}: {row.iloc[0][col]}\n")
                            matched = True
                            break
                break

        if not matched:
            print("❓ Sorry, I couldn't understand that. Try asking about a company and a keyword (e.g., 'Apple 2024 revenue growth').")

# Run it
ask_bot()
