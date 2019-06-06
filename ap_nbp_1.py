import requests

resp = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/gbp/last/10/?format=json")
#resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/today/")
result = resp.json()
#print(result)
def show_me_gbp():
    index = 0
    for i in result:
        #print(result['currency'][i])
        print(result['rates'][index]['no']," = ", result['rates'][index]['mid'])
        index = index + 1

show_me_gbp()