#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:56

from flask import Blueprint,render_template,g
from common.libs.helpler import ops_render
route_index = Blueprint('index_page',__name__)

@route_index.route('/')
def index():
    return ops_render('index/index.html')