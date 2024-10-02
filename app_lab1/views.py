from flask import jsonify
from datetime import datetime
from app_lab1 import app

@app.route('/healthcheck', methods=['GET'])
def helthcheck():
    return jsonify({
        "status": "OK",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }),200