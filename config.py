import os

from dotenv import load_dotenv

load_dotenv()

tg_token = os.getenv("tg_token")

url = 'https://api.rating.chgk.net/players?page=1&itemsPerPage=30&toBeChecked=false'
