from flask import Blueprint, redirect, render_template
from ..forms import AnswerForm
from test import db
from datetime import datetime
from ..models import Answer

answer = Blueprint('answer', __name__, url_prefix="/answer")

@answer.route("/create", methods=["GET", "POST"])
def create():
    # AnswerForm으로 화면에서 받은 데이터를
    form = AnswerForm()
    # 우리가 요청한 조건에 맞으면
    if form.validate_on_submit():
        a = Answer(question_id=1, content=form.content.data, create_date=datetime.now())
        # DB에 저장
        db.session.add(a)   
        db.session.commit()  
    # 후 원래 페이지로 redirect ('submit.html')
        return redirect ('submit.html')
    # 빈 화면으로 넘기기
    return render_template('answer/answer_form.html', form=form)