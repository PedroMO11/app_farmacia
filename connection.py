DB_HOST = 'localhost'
DB_PORT = '3306'
DB_USER = 'root'
DB_PASSWORD = 'mysql2023'
DB_SCHEMA = 'farmacia'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PASSWORD,DB_HOST,DB_PORT,DB_SCHEMA)