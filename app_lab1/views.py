from flask import jsonify
from datetime import datetime
from app import app

@app.route('.healthcheck', mathods=['GET'])
def helthcheck();
    return jsonify({
        "status": "OK",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }),200