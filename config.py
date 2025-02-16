import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "":)

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24023484"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "550aff09078aeff5cabe6f8716566d94")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6262184016"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://baijukumarsingh7463:KGARQDTRfS6NkrV5@cluster0.jxahs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
