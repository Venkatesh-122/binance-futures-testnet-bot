import os
import sys
import argparse
from dotenv import load_dotenv
from bot.logging_config import logger
from bot.orders import place_order

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Simple Binance Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, default=None)
    
    args = parser.parse_args()
    
    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        print("Error: API keys missing from .env file!")
        sys.exit(1)
        
    print(f"--- Order Request Summary ---")
    print(f"Symbol: {symbol} | Side: {side} | Type: {order_type} | Qty: {args.quantity}")
    
    try:
        result = place_order(symbol, side, order_type, args.quantity, args.price, api_key, api_secret)
        
        print("\nSUCCESS!")
        print(f"Order ID: {result.get('orderId')}")
        print(f"Status: {result.get('status')}")
        print(f"Executed Qty: {result.get('executedQty')}")
        print(f"Avg Price: {result.get('avgPrice')} USDT")
        
    except Exception as e:
        print(f"\nFAILURE: {e}")
        logger.error(f"Order failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()