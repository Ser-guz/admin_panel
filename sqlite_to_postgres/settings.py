import os
import dotenv

dotenv.load_dotenv('.env')

dsl = {
        'dbname': os.getenv('DB_NAME'),
        # 'user': os.getenv('USER'),
        'user': 'app',
        'password': os.getenv('PASS'),
        'host': os.getenv('HOST'),
        'port': os.getenv('PORT'),
    }
