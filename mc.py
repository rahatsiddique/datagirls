import quandl
quandl.ApiConfig.api_key = 'qe_zYg_VZHnH5SEzVML_'
quandl.ApiConfig.api_version = '2015-04-09'

data=quandl.get('LME/PR_CU')

print data

import quandl
# data = quandl.get_table('ZACKS/FC', ticker='AAPL')
