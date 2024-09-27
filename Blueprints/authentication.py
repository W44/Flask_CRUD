from http import HTTPStatus
from http.client import HTTPResponse
import json
from textwrap import indent
from tokenize import Name
from flask import Flask, Response, render_template, request, redirect
from Blueprints import authentication
# from flask_sqlalchemy import SQLAlchemy
from extensiondb import db
from Models.models import ProductLst, Users,Token
import jwt # import jwt library
import datetime
from flask import Response, request
from flask_jwt_extended import create_access_token
SECRET_KEY = "python_jwt"
from flask_jwt_extended import jwt_required, get_jwt_identity
# json data to encode


@authentication.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        temp_user = Users()
        temp_json = request.json

        temp_user.Name = temp_json["Name"]
        temp_user.password = temp_json["Password"]
        temp_user.permission = temp_json["Permission"]
        to_check = Users.query.filter_by(Name=temp_user.Name, password=temp_user.password).first()
        if to_check is None:
            temp_user.hash_password()
            db.session.add(temp_user)
            db.session.commit()
            return Response("<p> User sucessfully registered </p>", HTTPStatus.OK)
        else:
            return Response("<p> User already Present</p>", HTTPStatus.CONFLICT)
    elif request.method == "GET":
        temp_user = Users()
        to_auth = Users.query.filter_by(Name=request.args.get("Name")).first()
        if to_auth is not None:
            temp_user.Name = to_auth.Name
            temp_user.password = to_auth.password
            x=44
            temp_user.sno = to_auth.sno
            temp_user.permission = to_auth.permission
            authorize = temp_user.check_password(request.args.get("Password"))
            if not authorize:
                return Response("<p>Username or password incorrect</p>", HTTPStatus.NON_AUTHORITATIVE_INFORMATION)

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(temp_user.sno), expires_delta=expires)
            return Response(access_token, HTTPStatus.OK)
        else:
            return Response("<p>User Not Found</p>", HTTPStatus.NOT_FOUND)

    return Response("<p>request Method not supported</p>", HTTPStatus.METHOD_NOT_ALLOWED)


def AutherizeDecor(func):
    def inner(*args, **kwargs):
        temp_token = Token()
        user_id = get_jwt_identity()
        to_auth_user = Users.query.filter_by(sno=user_id).first()
        if to_auth_user is not None:
            if to_auth_user.permission is "A":  # and to_auth.permission is not "U"
                print("in decorator:Authorize")
                return func(*args, **kwargs)
            else:
                return Response("", HTTPStatus.NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response("", HTTPStatus.FAILED_DEPENDENCY)

    inner.__name__ = func.__name__
    return inner


def AuthenticateDecor(func):
    def inner(*args, **kwargs):
        temp_token = Token()
        to_auth = Token.query.filter_by(token=request.headers["Authorization"].split(" ")[1]).first()
        to_auth_user = Users.query.filter_by(sno=to_auth.sno).first()
        if to_auth_user is not None:
            if to_auth is not None:
                temp_token.sno = to_auth.sno
                temp_token.token = to_auth.token
                print("in decorator:Authenticate")
                return func(*args, **kwargs)
            else:
                return Response("", HTTPStatus.NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response("", HTTPStatus.FAILED_DEPENDENCY)

    inner.__name__ = func.__name__
    return inner
