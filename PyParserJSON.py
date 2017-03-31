#-*-coding:utf-8


from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
url = 'http://api.openweathermap.org/data/2.5/forecast'
service_key = 'de82d6d4bc81413bce54f58ec194befb'
cityid = '1835847'


queryParams = '?' + urlencode({quote_plus('id') : cityid}) + '&' + urlencode({quote_plus('APPID') : service_key})
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

print(response_body)




