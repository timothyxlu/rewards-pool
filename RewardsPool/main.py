# -*- coding: utf-8 -*-
from bottle import route, run, response, request

@route('/update_user')
def update_user():
    email = request.query.email
    available_credit = request.query.available_credit
    pc_progress = request.query.pc_progress
    mobile_progress = request.query.mobile_progress
    response.content_type = 'application/json'
    return "OK"

@route('/get_next_user')
def get_next_user():
    rv = {'first_name':'Xiaotian','email':'wind.zju@hotmail.com','passwd':'wind_518518'}
    response.content_type = 'application/json'
    return rv

@route('/signup')
def signup():
    rv = {'email':'wind.zju@hotmail.com','passwd':'wind_518518'}
    return rv

run(host='localhost', debug=True)  