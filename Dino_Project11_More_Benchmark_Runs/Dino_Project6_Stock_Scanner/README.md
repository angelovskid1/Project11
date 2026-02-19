# Python Stock Check Scanner - Project 6

The goal of this project is to look for swing trading opportunity.





A Python-based tool to scan stock market symbols and determine Bull/Bear market status using Technical Indicators (SMA 200, EMA 50/125).

## Features
*   **SMA 200 Trend Analysis**: Checks if price is above SMA 200 and if the SMA is rising.
*   **EMA Crossover**: Detects "Golden Cross" alignment (EMA 50 > EMA 125) and separation.
*   **Market Benchmark**: Automatically checks VOO/SPY for 1, 3, and 5-year trends.
*   **Reports**: Generates a console table and a CSV export (`stock_report.csv`).

## Installation

1.  **Prerequisites**: Python 3.8+
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the scanner:
```bash
python main.py
```

The script will:
1.  Check VOO (S&P 500) trend.
2.  Scan the hardcoded watchlist in `main.py`.
3.  Print a summary table.
4.  Save detailed results to `stock_report.csv`.

## Project Structure
*   `main.py`: Entry point, defines symbol list.
*   `scanner.py`: Core scanning loop and reporting.
*   `indicators.py`: Technical analysis logic.
*   `requirements.txt`: Python package dependencies.
