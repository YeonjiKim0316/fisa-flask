from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# app.py인 곳을 입구로 찾아서 기본적으로 실행합니다
# 또는 FLASK_APP이라는 환경변수의 이름을 파일명으로 변경합니다
# set FLASK_APP=test 
# wsgi.py에 직접 키=밸류로 여러 환경변수들을 기입합니다.

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(): # 어플리케이션 팩토리 - 플라스크 서버가 실행될 때 가장 최초로 실행되는 생성자
    test = Flask(__name__)

    # ORM
    test.config.from_object(config)
    db.init_app(test)
    migrate.init_app(test, db)

    # 블루프린트
    from .views import main_views, board_views, answer_views  # views 폴더 및의 main_views.py 임포트
    test.register_blueprint(main_views.bp)
    test.register_blueprint(board_views.board)
    test.register_blueprint(answer_views.answer)
    return test