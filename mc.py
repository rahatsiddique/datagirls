import quandl
quandl.ApiConfig.api_key = 'qe_zYg_VZHnH5SEzVML_'
quandl.ApiConfig.api_version = '2015-04-09'

data=quandl.get('NSE/OIL')

print data
