import StringIO
import base64


import quandl

def get_commod_data():
    quandl.ApiConfig.api_key = '3tWQBLpyDZsoV-TxKWH8'
    quandl.ApiConfig.api_version = '2015-04-09'

    data = quandl.get('WGEC/WLD_GOLD')
        # data = quandl.get_table('ZACKS/FC', ticker='AAPL')
    print data

