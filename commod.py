import StringIO
import base64

import quandl

def get_commod_data():
    quandl.ApiConfig.api_key = '3tWQBLpyDZsoV-TxKWH8'
    quandl.ApiConfig.api_version = '2015-04-09'

    data = quandl.get('NSE/OIL')

    # data = quandl.get_table('ZACKS/FC', ticker='AAPL')

    return data

def chart ():
    x = data["date"].tolist()
    y = data["high"].tolist()
    return render_template('chart.html', y=y, x=x)

data = get_commod_data()
col1 = get_col_1()
col2 = get_col2()

print(col1)
print(col2)
