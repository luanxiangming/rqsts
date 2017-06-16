# -*- coding: UTF-8 -*-
import requests
import json
from settings_stg import SettingsStg

''' vipjr: Register -> Activation -> Login'''

settings = SettingsStg()

account = 'usernamez@test.com'
password = '123456'
brandId = 4


def try_post(url, payload, timeout):
	try:
		r = requests.post(url, json=payload, timeout=timeout)
	except requests.ConnectionError:
		print("ConnectionError..." + "\n\n")
	except requests.Timeout:
		print("TimeOut..." + "\n\n")
	else:
		return r


def register(brandId, account, password, gender=1, mobile='111', phone='', SourceType='vipabc-vipabc'):
	url = settings.LoginHost + '/loginapi/register'
	cname = account[:account.index(u'@')]
	print("cname: " + cname)
	ename = cname
	payload = {
		'age': 20,
		'brandId': brandId,
		'cname': cname,
		'ename': ename,
		'countryId': u'+86',
		'email': account,
		'gender': gender,
		'parentMail': u"",
		'password': password,
		'mobile': mobile,
		'reasonId': u'111',
		'SourceType': SourceType,
		'birthday': u'',
		'phone': phone,
		'parentFlag': 0
	}
	r = try_post(url, payload, 10)
	print(r.text)
	if r.json()['success'] == True:
		print(account + " --- registered successfully!")
	else:
		print(account + " --- registered failed!")


def get_checkid(account):
	url = settings.APIStore + u'/VMD/VipJr.API/api/Client/GetClientBasicInfoByEmail'
	payload = {'email': account}
	r = try_post(url, payload, 3)
	JsonResult = r.json()[u'JsonResult']
	checkid = JsonResult[JsonResult.index('Randstr') + 10: JsonResult.index('Nlevel') - 3]
	return checkid


def ActivatingAccount(account):
	url = settings.APIHost + u'/Customer/ActivatingAccount'
	checkid = get_checkid(account)
	print('Checkid: ' + checkid)
	payload = {'checkid': checkid, 'client': account}
	r = try_post(url, payload, 10)
	print(r.text)
	if r.status_code == requests.codes.ok:
		print(account + " --- activated successfully!")
	else:
		print(account + " --- activated failed!")


def NewLogin(account, password):
	url = settings.APIHost + u'/Login/NewLogin'
	payload = {'Account': account, 'Password': password, 'RememberMe': False, 'FromIms': False}
	r = try_post(url, payload, 5)
	print(r.json())
	if r.json()['State'] == u'LOGIN_SUCCESS':
		print(account + " --- login successfully!")
	else:
		print(account + " --- login failed!")


register(brandId, account, password)
ActivatingAccount(account)
NewLogin(account, password)
