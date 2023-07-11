import requests

per= 'https://api.stackexchange.com/questions' #fromdate=2023-07-09&todate=2023-07-10&order=desc&sort=activity&tagged=Python&filter=default&site=stackoverflow'
params= {'fromdate': '2023-07-09', 'todate': '2023-07-10', 'site':'stackoverflow', 'tagged':'Python'}
response=requests.get(per, params=params)
print(response.status_code)
gh=response.json()["items"]
for i in gh:
    print(i.get( "title"))









