import pandas as pd
import yfinance as yf

def get_historical_data(symbol, period="5y"):
    """
    Fetches historical data for a given symbol.
    """
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period)
        if df.empty:
            print(f"Warning: No data found for {symbol}")
            return None
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def calculate_sma(df, window=200):
    """
    Calculates Simple Moving Average.
    """
    return df['Close'].rolling(window=window).mean()

def calculate_ema(df, window):
    """
    Calculates Exponential Moving Average.
    """
    return df['Close'].ewm(span=window, adjust=False).mean()

def analyze_trend(df):
    """
    Analyzes the trend based on SMA 200 and EMA 50/125.
    Returns a dictionary with status.
    """
    if df is None or len(df) < 200:
        return {
            "sma_200_trend": "Insufficient Data",
            "ema_cross_status": "Insufficient Data",
            "overall_status": "Unknown"
        }

    # Calculate Indicators
    df['SMA_200'] = calculate_sma(df, 200)
    df['EMA_50'] = calculate_ema(df, 50)
    df['EMA_125'] = calculate_ema(df, 125)

    # Get latest values and previous values for slope/trend
    current_close = df['Close'].iloc[-1]
    
    # SMA 200 Trend
    # Check if SMA 200 is rising (current > 5 days ago)
    sma_200_current = df['SMA_200'].iloc[-1]
    sma_200_prev = df['SMA_200'].iloc[-5] # 5 day lookback for slope
    
    is_above_sma = current_close > sma_200_current
    is_sma_rising = sma_200_current > sma_200_prev
    
    if is_above_sma and is_sma_rising:
        sma_status = "Bullish (Above & Rising)"
    elif is_above_sma and not is_sma_rising:
        sma_status = "Neutral (Above & Flat/Falling)"
    elif not is_above_sma and is_sma_rising:
        sma_status = "Neutral (Below & Rising)"
    else:
        sma_status = "Bearish (Below & Falling)"

    # EMA Cross Analysis
    ema_50 = df['EMA_50'].iloc[-1]
    ema_125 = df['EMA_125'].iloc[-1]
    
    # Check slope of EMAs
    ema_50_prev = df['EMA_50'].iloc[-5]
    ema_125_prev = df['EMA_125'].iloc[-5]
    
    emas_rising = (ema_50 > ema_50_prev) and (ema_125 > ema_125_prev)
    bullish_stack = ema_50 > ema_125
    
    if bullish_stack and emas_rising:
        ema_status = "Bullish (50 > 125 & Rising)"
    elif bullish_stack and not emas_rising:
        ema_status = "Weak Bullish (50 > 125 & Not Rising)"
    elif not bullish_stack:
        ema_status = "Bearish (50 < 125)"
    else:
        ema_status = "Neutral"

    # Overall Conclusion
    if "Bullish" in sma_status and "Bullish" in ema_status:
        overall = "BULL MARKET"
    elif "Bearish" in sma_status and "Bearish" in ema_status:
        overall = "BEAR MARKET"
    else:
        overall = "NEUTRAL/MIXED"

    return {
        "current_price": round(current_close, 2),
        "sma_200": round(sma_200_current, 2) if pd.notna(sma_200_current) else None,
        "ema_50": round(ema_50, 2),
        "ema_125": round(ema_125, 2),
        "sma_200_trend": sma_status,
        "ema_cross_status": ema_status,
        "overall_status": overall
    }
