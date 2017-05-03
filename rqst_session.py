import requests
import json

''' persist some cookies across requests '''
''' login -> MyLessons '''
payload = {'Account': 'usernamem@gmail.com', 'Password': '111111', 'RememberMe': False, 'FromIms': False}

''' This will make sure the session is closed as soon as the with block is exited, even if unhandled exceptions occurred. '''
with requests.Session() as s:
	try:
		s.post('http://stage.vipjr.com/Login/NewLogin', data=payload, timeout=5)
		r = s.post('http://stagemember.vipjr.com/aspx/IMO/MyLessons/PreparePage', timeout=5)
	except requests.ConnectionError:
		print("ConnectionError..." + "\n\n")
	except requests.Timeout:
		print("TimeOut..." + "\n\n")
	else:
		print("Request headers: ")
		for k,v in r.request.headers.items():
			print("\t" + k + ": " + v)
		print("Response headers: ")
		for k,v in r.headers.items():
			print("\t" + k + ": " + v)
		print(r.encoding)
		print(str(r.status_code))
		print(r.text)

''' Requests will throw a SSLError if it's unable to verify the certificate '''
try:
	requests.get('https://requestb.in', timeout=2)
except requests.exceptions.SSLError:
	print("SSL Error...")

''' GitHub does though '''
try:
	requests.get('https://github.com', timeout=2)
except requests.exceptions.SSLError:
	print("SSL Error...")

''' ignore verifying the SSL certificate '''
try:
	requests.get('https://kennethreitz.org', verify=False, timeout=2)
except requests.exceptions.SSLError:
	print("SSL Error...")

''' defer downloading the response body until you access the Response.content attribute with the stream parameter '''
tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
r = requests.get(tarball_url, stream=True, timeout=3)
# At this point only the response headers have been downloaded and the connection remains open
print(r.headers)
if int(r.headers['content-length']) < 100:
  	print(r.text)

''' Proxies '''
# To use HTTP Basic Auth with your proxy, use the http://user:password@host/ syntax:
# proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}
proxies = {
  'http': 'http://192.168.23.199:8080',
  'https': 'http://192.168.23.199:8080',
}
try:
	# Specify a tuple if you would like to seperate the 'connect' and 'read' timeouts:
	r = requests.get('https://www.google.com', proxies=proxies, timeout=(3, 5))
except requests.ConnectionError:
	print("ConnectionError..." + "\n\n")
except requests.Timeout:
	print("TimeOut..." + "\n\n")
else:
	print(r.text)

''' HTTP Verbs '''
r = requests.get('https://api.github.com/repos/kennethreitz/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad', timeout=3)
if r.status_code==requests.codes.ok:
	print(r.json())
	print(r.json().keys())
	print(r.json()['committer'])
	print(r.json()['message'])
verbs = requests.options(r.url)
print("Verb's status code: " + str(verbs.status_code))

r = requests.get('https://api.github.com/repos/kennethreitz/requests/issues/482')
issue = json.loads(r.text)
print(issue.keys())
print(issue[u'title'])
print(issue[u'comments'])

r = requests.get(r.url + u'/comments')
print(r.json()[2].keys())
print(r.json()[2][u'body'])
print(r.json()[2][u'user'][u'login'])



