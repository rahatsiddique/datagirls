from flask import Flask, render_template
app= Flask (__name__)

import quandl

def get_commod_data():
    quandl.ApiConfig.api_key = '3tWQBLpyDZsoV-TxKWH8'
    quandl.ApiConfig.api_version = '2015-04-09'

    data = quandl.get('FRED/SIPOVGINIDEU')
    return data

@app.route('/')
def index():
    return render_template("index.html")

@app.route ('/commodities')
def commodities():
    commodities = ["Oil" , "Steel", "Gold"]
    return render_template("commodities.html", commodities=commodities)

@app.route ('/graphs')
def chart():
    data = get_commod_data()

    col_1 = data["Value"].tolist()
    col_2 = range(len(col_1))

    print col_1
    print col_2


    return render_template("commodities.html", y=col_2, x=col_1)


if __name__=="__main__":
    app.run()