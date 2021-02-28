from flask import Blueprint, jsonify
from .services import ShowServices

show = Blueprint('show', __name__)


@show.route('/show', methods=['GET'])
def trigger():
    ShowServices().activate_job()
    return jsonify({
        "status": True
    })
