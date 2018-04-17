from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

import quandl

def get_commod_data():
    quandl.ApiConfig.api_key = '3tWQBLpyDZsoV-TxKWH8'
    quandl.ApiConfig.api_version = '2015-04-09'

    data = quandl.get('WGEC/WLD_GOLD')
    data1 = quandl.get('WGEC/WLD_WOODPULP')
    data2 = quandl.get('WGEC/WLD_SILVER')
    data3 = quandl.get('WGEC/WLD_NICKEL')
    return data

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template ("About_us.html")

@app.route ('/commodities')
def commodities():
    commodities = ["Oil" , "Steel", "Gold"]
    return render_template("commodities.html", commodities=commodities)

@app.route ('/graph')
def graph():
    data = get_commod_data()

    col_1 = data["Value"].tolist()
    col_2 = range(len(col_1))

    return render_template( "graph.html", labels=col_2, values=col_1, title='Gold price', arrays="numpy", paginate=True, min=20, max=1000)

if __name__== "__main__":
    app.run(debug=True)