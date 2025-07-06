# config.py
class Config:
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'your-jwt-secret'
    MONGODB_SETTINGS = {
        'db': 'batabase_name',
        'host': 'localhost',
        'port': 27017
    }
    # ยังไม่ได้ใช้