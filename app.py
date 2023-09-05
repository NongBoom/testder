from flask import Flask, render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def index(): #โมดูลรับค่าจากไฟล์ index.html โดยการส่งค่าในรูปแบบ POST
    return render_template('index.html')
@app.route('/save', methods=['POST'])
def save(): #โมดูลแสดงข้อมูล
    x = dict(request.form.items())
    return " %s"%(x)

app.run(debug=True)