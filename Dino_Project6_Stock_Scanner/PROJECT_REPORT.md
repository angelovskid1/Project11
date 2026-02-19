# Project 6: Python Stock Market Scanner - Engineering Report
**Author:** Dino Angelovski
**Date:** January 24, 2026

---

## Executive Summary
This project involves building a Python-based stock scanner to identify Bull/Bear market trends using technical indicators (SMA 200, EMA 50/125). The goal is to scan a specific list of stocks and ETFs, compare them against market benchmarks (VOO/SPY), and generate a status report.

## Technical Architecture
*   **Language:** Python
*   **Data Source:** `yfinance` (Yahoo Finance API)
*   **Analysis:** `pandas` for vectorised calculations
*   **Indicators:**
    *   **SMA 200:** Utilized for long-term trend direction (Slope check).
    *   **EMA 50 & 125:** Utilized for crossover/trend confirmation.

## Implementation Details

### 1. Project Structure
The project is isolated in `stock_scanner_py/` to maintain separation from the previous Node.js implementation.

### 2. Dependencies
*   `yfinance`: Chosen for easy access to historical market data.
*   `pandas`: Essential for efficient time-series analysis and rolling window calculations.

---

## Technical Challenges & Resolutions
*(To be populated as development progresses)*

## Results
**Status:** Verification Successful
**Date:** January 24, 2026
The scanner was successfully executed against the defined watchlist.
*   **Market Check:** VOO analysis for 1, 3, and 5 years completed.
*   **Watchlist:** 30+ symbols processed.
*   **Output:** Generated `stock_report.csv` and console table.

Key Observations from Initial Run:
*   **NVDA:** Bull Market (Above SMA 200, EMAs Rising)
*   **MSFT/Meta:** Neutral/Mixed (Price correction below SMA, but EMAs showing mixed signals).

