import os
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST, TimeFrame

# טוען את הקובץ config.env
load_dotenv("config.env")

api_key = os.getenv("ALPACA_API_KEY")
secret_key = os.getenv("ALPACA_SECRET_KEY")
base_url = os.getenv("ALPACA_BASE_URL")

api = REST(api_key, secret_key, base_url, api_version='v2')

# בדיקה פשוטה - קבלת פרטי החשבון
account = api.get_account()
print("Status:", account.status)
print("Equity:", account.equity)
