# -*- coding: UTF-8 -*-
import requests
import json
from settings_stg import SettingsStg
from requests_ntlm import HttpNtlmAuth
import mail

''' Product Order'''

settings = SettingsStg()

# Get Cookie
def login(s):
	try:
		s.auth = HttpNtlmAuth('vipabc\\oliverluan','SYS2012health', s)
		payload = {'ReturnUrl': '/ProductBuy/Index?ImsUrl=http%3a%2f%2fstageims.vipabc.com%2fasp%2fbd%2fproduct_buy.asp%3fclient_sn%3d1654157%26lead_sn%3d7682084%26hash%3d696CC6AEE22F01586D031A7254C3C795F6D16B17'}
		r = s.get('http://stage-imsp-content.vipabc.com/Account/Login', params=payload, timeout=5)
		print("Request headers: ")
		for k,v in r.request.headers.items():
			print("\t" + k + ": " + v)
		print("Response headers: ")
		for k,v in r.headers.items():
			print("\t" + k + ": " + v)
	except requests.ConnectionError:
		print("ConnectionError..." + "\n\n")
	except requests.Timeout:
		print("TimeOut..." + "\n\n")

# Get all products	
def CfgProductRequest(s):
	payload = {
		'staffSn': 16914,
		'okReason': 0,
		'contractSn': 0,
		'prowerSessionContractSn': 0,
		'unlimitedCardContractSn': 0,
		'clientSn': '1654157',
		'originalContractSn': 0,
		'webSite': 'C',
		'selectedProductSn': 0,
	}
	r = s.post('http://stage-imsp-content.vipabc.com/Api/CfgProductRequest', data=payload, timeout=5)
	for index, product in enumerate(r.json()['Data']):
		print(index, product['Sn'], product['ProductName'], product['TotalCash'])
	
	
def main():
	
	with requests.Session() as s:
		login(s)
		CfgProductRequest(s)
	# mail.send_mail('成功', '成功')

main()