from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.u0bki.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('mountain.html', msg='hi')

# @app.route("/mars", methods=["POST"])
# def mountain_post():
#     mountain_receive = request.form['mountain_give']
#     db.mountain.insert_one(mountain_receive)
#     return jsonify({'msg': 'POST 연결 완료!'})
#
# if __name__ == '__main__':
#    app.run('0.0.0.0', port=5000, debug=True)