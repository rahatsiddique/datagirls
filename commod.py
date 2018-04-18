

import quandl
import pandas as pd
def get_commod_data():
    quandl.ApiConfig.api_key = '3tWQBLpyDZsoV-TxKWH8'
    quandl.ApiConfig.api_version = '2015-04-09'

    data = quandl.get('WGEC/WLD_GOLD')
    #data1 = quandl.get( 'WGEC/WLD_WOODPULP' )
    #data2 = quandl.get( 'WGEC/WLD_SILVER' )
    #data3 = quandl.get( 'WGEC/WLD_NICKEL' )
        # data = quandl.get_table('ZACKS/FC', ticker='AAPL')
    print data
    dataDict = data.to_dict('split')
    #newdict = {1: 0, 2: 0, 3: 0}
    #print dataDict.values()
    timestampsList = dataDict["index"]
    dataList = dataDict["data"]
    #time_str=str(timestampsList)
    #year=time_str[:4]
    #timelessList = [i.split()[0] for i in timestampsList]
    dateList = [pd.to_datetime(i).strftime( '%Y') for i in timestampsList]
    print dateList
    print dataList
    #print timelessList
    #print year
    #print data1
    #print data2
    #print data3

get_commod_data()