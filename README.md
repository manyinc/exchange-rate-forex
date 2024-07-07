This Python script fetches real-time stock data for USD/JPY exchange rate using Yahoo Finance API (yfinance). It continuously monitors the opening price every minute and displays an arrow indicating whether the current opening price is higher or lower than the previous minute's opening price.

## Requirements
- Python 3.x
- yfinance library (install via `pip install yfinance`)

## Installation
1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).
2. Install the required `yfinance` library by running:
   ``` bath
   pip install yfinance
   ```
3. Download the script `exchange-rate-forex` from this repository.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the script using Python:
``` bath
python main.py
```
## Notes
- The script clears the screen (`cls` or `clear`) to update the display every minute.
- It uses color codes (`color 0A` for up and `color 0C` for down) to visually indicate price movements.
- The script runs indefinitely until interrupted (e.g., with Ctrl+C).

## Disclaimer
- This script is for educational purposes only. Use it at your own risk.
