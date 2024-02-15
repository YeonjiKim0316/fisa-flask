from flask import Blueprint, redirect, render_template, url_for, g 
from ..forms import AnswerForm
from test import db
from datetime import datetime
from ..models import Answer

answer = Blueprint('answer', __name__, url_prefix="/answer")

@answer.route("/create/<int:question_id>", methods=["GET", "POST"])
def create(question_id):
    # AnswerForm으로 화면에서 받은 데이터를
    form = AnswerForm()
    # 우리가 요청한 조건에 맞으면
    if form.validate_on_submit():
        a = Answer(question_id=question_id, \
                   content=form.content.data, \
                    create_date=datetime.now(),
                    user=g.user)
        # DB에 저장
        db.session.add(a)   
        db.session.commit()  
    # 후 원래 페이지로 redirect ('submit.html')
        return redirect (url_for ('board.post_detail', question_id=question_id))
    # 빈 화면으로 넘기기
    return render_template('question/question_detail.html', question_id=question_id, form=form)