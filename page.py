from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

import quandl

def get_commod_data(getcmd):
    quandl.ApiConfig.api_key = '3tWQBLpyDZsoV-TxKWH8'
    quandl.ApiConfig.api_version = '2015-04-09'

    #data = quandl.get('WGEC/WLD_GOLD')
    #data1 = quandl.get('WGEC/WLD_WOODPULP')
    #data2 = quandl.get('WGEC/WLD_SILVER')
    #data3 = quandl.get('WGEC/WLD_NICKEL')
    data = quandl.get(getcmd)
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
    # data = quandl.get('WGEC/WLD_GOLD')
    # data1 = quandl.get('WGEC/WLD_WOODPULP')
    # data2 = quandl.get('WGEC/WLD_SILVER')
    # data3 = quandl.get('WGEC/WLD_NICKEL')
    data = get_commod_data('WGEC/WLD_GOLD')
    #data1 = get_commod_data( 'WGEC/WLD_WOODPULP' )
    #data2 = get_commod_data( 'WGEC/WLD_SILVER' )
    #data3 = get_commod_data( 'WGEC/WLD_NICKEL' )

    dataDict = data.to_dict( 'split' )

    timestampsList = dataDict["index"]
    dataList = dataDict["data"]

    print dataList
    print timestampsList

    #col_2 = range(len(col_1))
    return render_template( "graph.html",labels=timestampsList, values=dataList, title='Gold price', paginate=True,min=20, max=1700)

if __name__== "__main__":
    app.run(debug=True)