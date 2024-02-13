from flask import Blueprint, render_template
from ..models import Question, Answer

# 우리가 부를 이름, flask 프레임워크가 찾을 이름, 라우팅주소
board = Blueprint('board', __name__, url_prefix="/board")

@board.route("/post")
def post_list():
    question_list = Question.query.all()
    return render_template("question_list.html", question_list=question_list)

# board/detail/1 2 3 4  -> question_detail.html로 각 글의 실제 세부내용을 전달하고 싶어요
@board.route("/detail/<int:question_id>") # question_id 변수로 받은 값을 
def post_detail(question_id): # 함수의 파라미터로 전달
    # question = Question.query.get(question_id) # 모델에서 특정 번호(id)를 통해 값을 조회 
    question = Question.query.get_or_404(question_id)
    return render_template("question_detail.html", ques = question)