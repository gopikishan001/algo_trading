
def fetch_data(kite, symbol: str):
    full_symbol = symbol
    
    try:
        data = kite.quote([full_symbol])
        return data[full_symbol]
    except Exception as e:
        print(f"[ERROR] Failed to fetch data for {full_symbol} — {e}")
        return None
