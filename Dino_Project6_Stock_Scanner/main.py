from scanner import scan_market, print_report, export_to_csv

# List of symbols from user request
SYMBOLS = [
    "XLF", "XLE", "XLI", "XLU", "XLV", "XLP", "XLY", "XLC", "XLK", "XLRE", # Sectors
    "AVGO", "GOOG", "MNST", "CRM", "META", "LLY", "V", "ADBE", "NOW", "MAGS", # Tech/Growth
    "SMH", # Semi ETF
    "SPY", "QQQ", "VOO", "TQQQ", # Market Indices
    "QCOM", "PLTR", "MSFT", "SMCI", "AAPL", "TSLA", "NVDA" # High profile tech
]

def main():
    # User requested time ranges: 1, 3, 5 yr.
    # We'll default to 5y as it provides enough data for SMA 200 and long term EMA.
    # Ideally, SMA 200 requires at least ~1 year of trading days (252), so "1y" might be tight if not exactly 365 days or weekends.
    # "2y" or "5y" is safer for "Trend" analysis over long term.
    
    print("--- Python Stock Scanner ---")
    
    # Market Check (VOO)
    print("\n>>> Market Benchmark Check (VOO) <<<")
    # We scan VOO for multiple timeframes as requested
    market_results = []
    for tf in [1, 3, 5]:
        print(f"Checking VOO for {tf} Year(s)...")
        # Note: '1y' might barely have 200 data points if holidays exist, but yfinance usually handles it.
        # indicators.py checks len(df) < 200, so it handles safety.
        res = scan_market(["VOO"], lookback_years=tf)
        if res:
            res[0]['Timeframe'] = f"{tf}Y"
            market_results.extend(res)
            
    print_report(market_results)
    
    # Full Scan
    print("\n>>> Full Watchlist Scan (5 Year Data) <<<")
    results = scan_market(SYMBOLS, lookback_years=5)
    print_report(results)
    export_to_csv(results, "stock_report.csv")

if __name__ == "__main__":
    main()
