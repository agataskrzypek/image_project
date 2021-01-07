import requests
from requests.auth import HTTPBasicAuth

url = "https://restful-booker.herokuapp.com/auth"
json_file = {
    "username" : "admin",
    "password" : "password123"
}
out_token = requests.post(url=url, data=json_file)
out_ids = requests.get('https://restful-booker.herokuapp.com/booking')
out_id = requests.get('https://restful-booker.herokuapp.com/booking/4')
out_name = requests.get('https://restful-booker.herokuapp.com/booking?firstname=Eric&lastname=Wilson')

to_post = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
    "checkin" : "2018-01-01",
    "checkout" : "2019-01-01"
    }}
out_post = requests.post(url="https://restful-booker.herokuapp.com/booking", data=to_post, auth = HTTPBasicAuth(
    'admin', 'password123'))
out_put = requests.put('https://restful-booker.herokuapp.com/booking/4', data=to_post, auth = HTTPBasicAuth(
    'admin', 'password123'))

receive = requests.get('https://img.pakamera.net/i1/1/486/grafiki-i-ilustracje-12156277_2218152486.jpg')

with open(r'C:\Users\user\Edukacja\grafiki-i-ilustracje-12156277_2218152486.jpg','wb') as f:
    f.write(receive.content)


print('ssss')
print('sss2')

print('słodko')
pass