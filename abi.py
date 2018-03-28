import quandl
quandl.ApiConfig.api_key = 'Pa_FSySNzYbasYuBMoGy'
quandl.ApiConfig.api_version = '2015-04-09'

data = quandl.get('NSE/OIL')

print data
