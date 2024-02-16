import os
from dotenv import load_dotenv

# .env 안에 있는 환경변수들을 키=밸류로 엔터 단위대로 읽어오게 됩니다
load_dotenv()

mySecretKey=os.environ.get('SECRET_KEY')
BASE_DIR=os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI="sqlite:///{}".format(os.path.join(BASE_DIR, "test.db"))
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY = mySecretKey