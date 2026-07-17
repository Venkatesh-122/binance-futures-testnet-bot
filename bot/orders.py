from bot.client import send_api_request
from bot.logging_config import logger

def place_order(symbol, side, order_type, quantity, price, api_key, api_secret):
    """
    Validates inputs and builds the payload for the client layer.
    """
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")
    if order_type == "LIMIT" and not price:
        raise ValueError("LIMIT orders require a price")
        
    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": str(quantity)
    }
    
    if order_type == "LIMIT":
        payload["price"] = str(price)
        payload["timeInForce"] = "GTC"
        
    logger.info(f"Placing {order_type} {side} order for {symbol}")
    
    return send_api_request("POST", "/fapi/v1/order", payload, api_key, api_secret)