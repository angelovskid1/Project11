# Project 11: More Benchmark Runs

This project consolidates the extended benchmarking work for the Stock Scanner (Project 6) and Moving Average Backtest (Project 8).

## Directory Structure

-   **`Dino_Project6_Stock_Scanner/`**: Contains the stock scanner Python scripts.
    -   `main.py`: Main entry point.
    -   `scanner.py`: Core scanning logic (updated with timestamps).
    -   `indicators.py`: Technical indicator calculations.
    -   `stock_report.csv`: Output report with timestamp headers.

-   **`Dino_Project8_MA_Benchmark/`**: Contains the Moving Average backtesting scripts and results.
    -   `leo_backtest.py`: Core backtesting script (updated for CLI args and timestamps).
    -   `run_benchmarks.py`: Automation script to run all 3 benchmarks.
    -   `watchlist_leo_project7.csv`: Original watchlist.
    -   `rule40_stocks.csv`: New Rule of 40 stock list.
    -   `index_etfs.csv`: New Index ETF list.
    -   `outputs_original/`: Results for original watchlist.
    -   `output_stock/`: Results for Rule 40 stocks.
    -   `output_index/`: Results for Index ETFs.

## How to Run

### Project 6
```bash
cd Dino_Project6_Stock_Scanner
python main.py
```
Check `stock_report.csv` for results.

### Project 8
```bash
cd Dino_Project8_MA_Benchmark
python run_benchmarks.py
```
This will execute all three benchmark runs sequentially. Check the respective output directories.
