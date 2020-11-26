from flask import Flask
from flask import render_template

app = Flask(__name__)

def get_data():
    #把要呈現的數字字串寫在這裡
    data = "[1,2,4,5,8,5,2,1,4,5,6,8],[9,8,7,2,8,5,2,1,4,5,6,8],[9,8,7,2,8,5,2,1,4,5,6,8]"
    return data

@app.route("/")
def index():
    data = get_data()
    return render_template("line_chart.html",data=data)

if __name__ == "__main__":
    app.run()
