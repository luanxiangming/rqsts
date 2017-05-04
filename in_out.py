# -*- coding: utf-8 -*-

import requests
import time
import logging
import random
import mail

''' CHECK_IN_OUT '''

card_numbers = ['工号']
url = 'http://tpehrweb.tutorabc.com/TIMG_inout/form/SystemHttp.json'
log_file = 'log.txt'

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=log_file,
                filemode='a')

def check_inout(inout):
	for card_number in card_numbers:
		payload = {'card_number': card_number, 'inout': inout, 'handlerName': 'Index.Index', 'method': 'Check_InOUT'}
		time.sleep(random.randint(60, 600))
		try:
			r = requests.post(url, data=payload, timeout=3)
		except requests.ConnectionError:
			logging.info("ConnectionError..." + "\n\n")
		except requests.Timeout:
			logging.info("TimeOut..." + "\n\n")
		else:
			logging.info(r.text)
			if inout==1 and r.status_code==requests.codes.ok:
				logging.info("Check In Succeed." + "\n\n")
			elif inout==0 and r.status_code==requests.codes.ok:
				logging.info("Check Out Succeed." + "\n\n")
		
def is_weekend():
	day = time.strftime('%w')
	if day in ['0', '6']:
		return True
	return False

def check_in_out():
	if not(is_weekend()):
		hour = time.strftime('%H')
		if int(hour) <= 12:
			check_inout(1)
			# mail.send_mail('签入成功', '签入成功')
		else:
			check_inout(0)
			# mail.send_mail('签出成功', '签出成功')
	else:
		logging.warning("It's weekend.")


check_in_out()