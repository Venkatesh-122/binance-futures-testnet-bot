```markdown
# Simple Binance Futures Testnet Trading Bot

A clean Python application to place MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M) using direct REST API calls.

## Project Structure
```text
trading_bot/
├─ .env
├─ bot/
│  ├─ __init__.py
│  ├─ client.py
│  ├─ logging_config.py
│  └─ orders.py
├─ cli.py
├─ logs/
│  └─ trading_bot.log
├─ README.md
├─ requirements.txt

```

---

## Setup Steps

### 1. Install Libraries

Activate your virtual environment (`venv`) and run:

```bash
pip install -r requirements.txt

```

### 2. Add API Keys

Create a file named `.env` in the root folder and add your credentials:

```text
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here

```

---

## How to Run Examples

### 1. Market Orders

```bash
# Market BUY
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005

# Market SELL
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.005

```

### 2. Limit Orders

```bash
# Limit BUY
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.005 --price 63000

# Limit SELL
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.005 --price 64500

```

---

## Assumptions & Design

* **Direct REST Calls:** Uses the `requests` library to connect directly to the Binance API instead of a heavy SDK.
* **HMAC-SHA256 Signing:** Requests are manually signed using Python's native `hmac` and `hashlib` modules.
* **Parameter Control:** The `price` and `timeInForce` parameters are dynamically added *only* for LIMIT orders to prevent API errors.
* **Logging:** All requests, responses, and errors are saved directly in `logs/trading_bot.log`.

```

```
