from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
	                # 화면에서 출력할 해당 필드의 라벨, 필수 항목 체크 여부
    # <label for='subject'> 제목 </label>
    # <input type=text name='subject' required> 
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    # subject = StringField('제목')
    # <label for='content'> 내용 </label>
    # <input typt=text-area name='content' required> 

    content = TextAreaField('내용', validators=[DataRequired()])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])