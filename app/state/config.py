from app.db.config_loader import ConfigLoader

class Config(ConfigLoader):
    PORT: int = 7654
    SQL_HOST: str = "localhost"
    SQL_PORT: int = 3306
    SQL_USER: str = "root"
    SQL_DB: str = "rosu"
    SQL_PASS: str = "db password"
    SRV_URL: str = "https://ussr.pl"
    SRV_NAME: str = "RealistikOsu"
    
config = Config()
