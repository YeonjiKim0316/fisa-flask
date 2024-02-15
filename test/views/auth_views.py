from flask import Blueprint, request, redirect, render_template, flash, url_for
from test.forms import UserCreateForm
from test.models import User
from test import db

auth = Blueprint('auth', __name__, url_prefix="/auth")
# __init__ 의 create_app 안에 등록


# 회원 가입 - signup
@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    #1. 폼을 가져온다
    form = UserCreateForm()

    ## update와 유사한 로직으로 작동합니다 
    #2-1. 폼의 유효성을 확인한다 & db에 해당하는 사용자이름이 있는지도 확인
    if form.validate_on_submit() and request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            #2-1-1. db의 user 테이블에 값을 넣는다  
            user = User(username=form.username.data, \
                        password=form.password1.data, \
                        email=form.email.data)                                                 
            db.session.add(user)
            db.session.commit()
            return redirect( url_for( 'main.index' ) )
        #2-1-2. 이미 존재하는 사용자입니다
        else:
            flash('이미 가입한 아이디입니다')
    #2-2. 다시 auth/signup.html로 이동시킵니다.
    return render_template('auth/signup.html', form=form)

# 로그인 - login
# @auth.route("/login")

# 로그아웃 - logout 
# @auth.route("/logout")