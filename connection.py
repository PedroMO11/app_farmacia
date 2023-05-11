DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASSWORD = '123'
DB_SCHEMA = 'farmacia'

DB_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PASSWORD,DB_HOST,DB_PORT,DB_SCHEMA)