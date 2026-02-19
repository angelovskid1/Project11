from indicators import get_historical_data, analyze_trend
import pandas as pd
from tabulate import tabulate

def scan_market(symbols, lookback_years=5):
    """
    Scans a list of symbols and returns a summary Erika_Project3_Report.
    """
    results = []
    
    print(f"Starting scan for {len(symbols)} symbols. Timeframes: {lookback_years}y...")
    
    for symbol in symbols:
        print(f"Scanning {symbol}...", end="\r")
        df = get_historical_data(symbol, period=f"{lookback_years}y")
        
        if df is None:
            results.append({
                "Symbol": symbol,
                "Status": "Error/No Data"
            })
            continue

        analysis = analyze_trend(df)
        
        # Flatten the dictionary for the Erika_Project3_Report
        row = {
            "Symbol": symbol,
            "Price": analysis.get("current_price"),
            "Status": analysis.get("overall_status"),
            "SMA Trend": analysis.get("sma_200_trend"),
            "EMA Condition": analysis.get("ema_cross_status"),
            "SMA 200": analysis.get("sma_200"),
            "EMA 50": analysis.get("ema_50"),
            "EMA 125": analysis.get("ema_125")
        }
        results.append(row)
    
    print("\nScan complete.")
    return results

def print_report(results):
    """
    Prints a formatted table of the results.
    """
    if not results:
        print("No results to display.")
        return

    # Create a DataFrame for nicer printing (optional, or just use tabulate directly list of dicts)
    df_results = pd.DataFrame(results)
    
    # Sort by Status for better readability
    if "Status" in df_results.columns:
        df_results.sort_values(by="Status", inplace=True)

    print("\n" + "="*80)
    print("STOCK MARKET SCANNER REPORT")
    print("="*80)
    print(tabulate(df_results, headers="keys", tablefmt="grid", showindex=False))
    print("\n")

def export_to_csv(results, filename="scan_results.csv"):
    import datetime
    
    # Generate timestamps
    now = datetime.datetime.now()
    iso_timestamp = now.isoformat()
    run_timestamp = now.strftime("%Y%m%d_%H%M%S")

    df = pd.DataFrame(results)
    
    # Write comments first, then CSV data
    with open(filename, 'w', newline='') as f:
        f.write(f"# generated_at={iso_timestamp}\n")
        f.write(f"# run_timestamp={run_timestamp}\n")
        df.to_csv(f, index=False)
        
    print(f"Results exported to {filename}")
