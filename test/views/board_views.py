from flask import Blueprint, render_template, url_for, redirect
from ..models import Question, Answer
from ..forms import QuestionForm, AnswerForm
from datetime import datetime
from test import db    

# 우리가 부를 이름, flask 프레임워크가 찾을 이름, 라우팅주소
board = Blueprint('board', __name__, url_prefix="/board")

@board.route("/list")
def post_list():
    question_list = Question.query.all()
    return render_template("question/question_list.html", question_list=question_list)

# board/detail/1 2 3 4  -> question_detail.html로 각 글의 실제 세부내용을 전달하고 싶어요
@board.route("/detail/<int:question_id>") # question_id 변수로 받은 값을 
def post_detail(question_id): # 함수의 파라미터로 전달
    # question = Question.query.get(question_id) # 모델에서 특정 번호(id)를 통해 값을 조회
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    return render_template("question/question_detail.html", question = question,  question_id = question_id, form=form)


@board.route('/create', methods=['GET', 'POST'])
def create():
    # 폼을 받는다
    form = QuestionForm()

    # 폼에 온 양식이 우리가 forms.py에 작성한 양식과 일치하는지 확인한다
    if form.validate_on_submit():
    # 일치하면 성공을 의미하는 주소로 전달한다
        # 실제 db에 값을 넣는 로직이 없습니다

       q = Question(subject=form.subject.data, \
                   content=form.content.data, \
                    create_date=datetime.now())                                                 
       db.session.add(q)
       db.session.commit()
       return redirect( url_for( 'board.post_list' ) )
       
       
    #    return render_template( 'question/question_list.html' )
    
    return render_template('question/question_form.html', form=form)


# @board.route("/create", methods=['GET', 'POST'])
# def create():
    # 폼을 받는다
  #  form 
    # 폼에 온 양식이 우리가 forms.py에 작성한 양식과 일치하는지 확인한다
    # 일치하면 성공을 의미하는 주소로 전달한다
