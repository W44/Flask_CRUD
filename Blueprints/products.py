from http import HTTPStatus
import json
# from urllib import response
from Blueprints import products
from flask import Flask, jsonify, render_template, request, redirect, Response
from Blueprints.products import products
from extensiondb import db
from Models.models import ProductLst
from Blueprints.authentication import AuthenticateDecor,AutherizeDecor
from flask_user import login_required,UserManager
from flask_jwt_extended import jwt_required, get_jwt_identity


@products.route("/", methods=[ "POST", "DELETE", "PUT"],endpoint="Myfunction")
@jwt_required()
@AutherizeDecor
def hello_world():
    if request.method == "POST":
        body_json = request.json

        myf1_db = ProductLst(Name=body_json["Name"], Price=body_json["Price"])
        to_check = ProductLst.query.filter_by(Name=body_json["Name"]).first()
        if to_check is None:
            myf1_db.save()
        all_products = ProductLst.query.all()
        temp_json = []
        for product in all_products:
            temp_json.append(json.dumps(product.to_dict(), indent=4))
        return Response(temp_json, HTTPStatus.OK)
    elif request.method == "DELETE":
        to_del = ProductLst.query.filter_by(sno=request.args.get("sno")).first()
        if to_del is not None:
            db.session.delete(to_del)
            db.session.commit()
            all_products = ProductLst.query.all()
            temp_json = []
            for product in all_products:
                temp_json.append(json.dumps(product.to_dict(), indent=4))
            return Response(temp_json, HTTPStatus.OK)
        return Response({}, HTTPStatus.NOT_FOUND)
    elif request.method == "PUT":
        product_name = request.args.get("name")
        product_price = request.args.get("price")
        to_update = ProductLst.query.filter_by(sno=request.args.get("sno")).first()
        if to_update is not None and to_update.Name != product_name and to_update.Price != product_price:
            to_update.Name = product_name
            to_update.Price = product_price
            db.session.add(to_update)
            db.session.commit()
            all_products = ProductLst.query.all()
            temp_json = []
            for product in all_products:
                temp_json.append(json.dumps(product.to_dict(), indent=4))
            return Response(temp_json, HTTPStatus.OK)
        else:
            all_products = ProductLst.query.all()
            temp_json = []
            for product in all_products:
                temp_json.append(json.dumps(product.to_dict(), indent=4))
            return Response(temp_json, HTTPStatus.CONFLICT)

    return Response({}, HTTPStatus.METHOD_NOT_ALLOWED)


@products.route("/", methods=["GET"],endpoint="Myfunction2")
@jwt_required()
def hello_world():
    to_return = ProductLst()
    result_filter = ProductLst.query.filter_by(sno=request.args.get("sno")).first()
    if result_filter is not None:
        to_return.sno = result_filter.sno
        to_return.Name = result_filter.Name
        to_return.Price = result_filter.Price
        product_dictionary = to_return.to_dict()
        return Response(json.dumps(product_dictionary, indent=4), HTTPStatus.OK)
    else:
        return Response({}, HTTPStatus.NOT_FOUND)


@products.route("/getall", methods=["GET"])
@jwt_required()
@AutherizeDecor
def get_all():
    all_products = ProductLst.query.all()
    temp_json = []
    for product in all_products:
        temp_json.append(json.dumps(product.to_dict(), indent=4))

    return Response(temp_json, HTTPStatus.OK)
