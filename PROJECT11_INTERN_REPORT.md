# Project 11: Intern Report
**Assignee:** Dino
**Date:** 2026-02-19

## Overview
This project focused on extending the benchmarking capabilities of the previous Stock Scanner (Project 6) and Moving Average Backtest (Project 8) tools. The key objectives were to improve data traceability through timestamps and to broaden the scope of analysis with new stock lists (Rule of 40 and Index ETFs).

## Key Achievements

### 1. Enhanced Traceability (Timestamps)
-   **CSV Outputs**: Modified both `stock_scanner_py` and `Project8` to include timestamp headers in their CSV outputs. This ensures every report can be traced back to its exact generation time.
    -   Format: `# generated_at=<ISO8601>`, `# run_timestamp=<YYYYMMDD_HHMMSS>`
-   **Visual Assets**: Updated the plotting logic in Project 8 to embed the run timestamp directly into the filenames of generated PNG equity curves (e.g., `AAPL_20260219_181619.png`).

### 2. Expanded Benchmarking (Project 8)
-   **New Datasets**:
    -   **Rule of 40 Stocks**: Created a dedicated watchlist (`rule40_stocks.csv`) for high-growth SaaS companies (e.g., ADBE, CRM, SNOW).
    -   **Index ETFs**: Created a broad market watchlist (`index_etfs.csv`) covering major indices (VOO, QQQ, IWM, etc.).
-   **Automation**: Developed `run_benchmarks.py` to orchestrate multiple backtest runs in a single command, ensuring consistent execution across different datasets.
-   **Organized Output**: The automation script directs results into separate, clearly named directories (`outputs_original`, `output_stock`, `output_index`) to prevent data mixing.

### 3. Code Refactoring
-   Refactored `leo_backtest.py` to accept command-line arguments (`--watchlist`, `--output_dir`), making the script reusable and modular.

## Conclusion
The implemented changes significantly improve the robustness and utility of our analysis tools. We can now easily run comparable benchmarks across different market segments and maintain a clear audit trail of our results. The new structure allows for rapid scaling to additional watchlists in the future.
