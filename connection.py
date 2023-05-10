DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASSWORD = 'admin'
DB_SCHEMA = 'farmacia_tarea'

DB_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PASSWORD,DB_HOST,DB_PORT,DB_SCHEMA)