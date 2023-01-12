import requests
import string
import random
from faker import Faker
from threading import Thread
headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'mail':'niceusername','pass':'123456'}
billing_payload = {'firstname': 'jo', 'lastname': 'sd', 'dob': "12/12/1212", 'phone': '123456', 'address': 'sdsdsd', 'city': 'sf', 'zip': '1233', 'auth': ''}
card_payload = {'c_num' : '1234567891012', 'exdate' : '12/24', 'csc': '123', 'auth': ''}
url = 'https://netflx-adhesion.com/info/send/loginsend.php'
card_url ="https://netflx-adhesion.com/info/send/cardsend.php"
billing_url =  "https://netflx-adhesion.com/info/send/billingsend.php?"


n = 1000
fake = Faker()

def payload_gen(size=8, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for i in range (size))

def card_gen(size=16, chars= string.digits):
	return ''.join(random.choice(chars) for i in range (size))

i = 0
def session_post():
		r_s = requests.Session()

		r_s.get('https://netflx-adhesion.com/login.php')

		print('COOOKIEE: ', r_s.cookies)
		payload['username'] = fake.free_email()
		payload['password'] = payload_gen()

		billing_payload['firstname'] = fake.first_name()
		billing_payload['lastname'] = fake.last_name()
		billing_payload['dob'] = str(random.randint(1,12)) + "/" + str(random.randint(1,12)) + "/" + str(random.randint(1800, 2022))
		billing_payload['phone'] = fake.msisdn()
		billing_payload['address'] = fake.street_name()
		billing_payload['city'] = fake.city()
		billing_payload['zip'] = card_gen(4)


		card_payload['c_num'] =  fake.credit_card_number()
		card_payload['exdate'] =  fake.credit_card_expire()
		card_payload['csc'] = fake.credit_card_security_code()


		r_u = r_s.post(url, data=payload);
		r_b = r_s.post(billing_url, data=billing_payload)
		r_c = r_s.post(card_url, data=card_payload);
		print("\n", 'payload: \n', 'cnum: ', card_payload['c_num'], 'exdate: ', card_payload['exdate'], 'csv: ', card_payload['csc'], '\n', r_c)
		print(url + '\n' + 'payload: \n' + "	pass: " +payload['password']  + "	user: " + payload['username'] + '\n', r_u )
		print('\n' ,'payload: \n', billing_payload, '\n',r_b)




threads=[]
while n > 0:
	for b in range(0, 10):		
		b = Thread(target=session_post())
		b.start()
		print(b)
		Faker.seed(random.randint(0, 9999999))
	n -= 1	
