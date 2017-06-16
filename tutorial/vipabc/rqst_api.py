import requests
import json
import time

print("\nSTART: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

''' GET '''
''' Timeouts '''
r = requests.get('http://172.16.233.82:8091/sessionBooking/getSessionrecordViewList?clientSn=566889', timeout=3)
print('\n' + r.url)
print('\t' + r.text)

''' POST '''
url = 'http://stageapistore.vipabc.com/VMD/VipJr.API/api/Client/GetClientInfoById'
payload = {'sn':'2602062'}
r = requests.post(url, data=payload, timeout=3)
r = requests.post(url, data=json.dumps(payload))
r = requests.post(url, json=payload)
print('\n' + r.url)
print('\t' + r.text)

''' PUT '''
r = requests.put('https://echo.getpostman.com/put', data = 'Etiam mi lacus', timeout=3)
print('\n' + r.url)
print('\t' + r.text)

''' DELETE '''
r = requests.delete('https://echo.getpostman.com/delete', timeout=3)
print('\n' + r.url)
print('\t' + r.text)

''' Passing Parameters In URLs '''
''' Response Status Codes '''
payload = {'profileId': 866, 'DCGSValid': 1}
r = requests.get('http://172.16.233.82:8091/sessionBooking/getDCGS', params=payload, timeout=3)
print('\n' + r.url)
print('\tEncoding: ' + r.encoding)
print('\tStatus: ' + str(r.status_code))
print('\t' + r.text)

''' Custom Headers '''
''' Response Headers '''
url = 'https://echo.getpostman.com/headers'
headers = {'my-sample-header': 'Lorem ipsum dolor sit amet'}
r = requests.get(url, headers = headers, timeout=3)
print('\n' + r.url)
print('\t' + r.text)
print('Response Headers: ')
for k,v in r.headers.items():
	print('\t' + k + ': ' + v)

''' Cookies '''
url = 'https://echo.getpostman.com/cookies'
r = requests.get(url, timeout=3)
print('Cookies: ')
print('\t' + r.cookies['sails.sid'])
for k,v in r.cookies.items():
	print('\t' + k + ': ' + v)

''' Redirection and History '''
inout = 1
r = requests.get('http://github.com', timeout=3)
print('\tStatus: ' + str(r.status_code))
if inout==1 and r.status_code==requests.codes.ok:
	print("\tHistory: ")
	for hsty in r.history:
		print(hsty.text)

r = requests.get('http://github.com', allow_redirects=False, timeout=3)
print('\tStatus: ' + str(r.status_code))
print("\tHistory: ")
for hsty in r.history:
	print(hsty.text)

