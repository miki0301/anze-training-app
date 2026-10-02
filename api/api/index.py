from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/python/test', methods=['GET'])
def test_api():
    return jsonify({
        "status": "success",
        "message": "安澤健康顧問系統 Python 後端已啟動！"
    })