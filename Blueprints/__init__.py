from flask import Blueprint


products = Blueprint("products",__name__,template_folder="../templates")
authentication = Blueprint("authentication",__name__,template_folder="../templates")