import subprocess
import os
import sys

def run_backtest(watchlist, output_dir):
    print(f"Running backtest for {watchlist} -> {output_dir}")
    cmd = [
        sys.executable, "leo_backtest.py",
        "--watchlist", watchlist,
        "--output_dir", output_dir
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully completed run for {watchlist}")
    except subprocess.CalledProcessError as e:
        print(f"Error running backtest for {watchlist}: {e}")

if __name__ == "__main__":
    # 1. Original Watchlist
    run_backtest("watchlist_leo_project7.csv", "outputs_original")
    
    # 2. Rule 40 Stocks
    run_backtest("rule40_stocks.csv", "output_stock")
    
    # 3. Index ETFs
    run_backtest("index_etfs.csv", "output_index")
    
    print("\nAll benchmarks completed.")
