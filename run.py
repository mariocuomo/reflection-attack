from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, current_app
from cryptography.fernet import Fernet

import random
import string

def get_random_challenge():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(20))
    return result_str


app = Flask(__name__)
connection_request={}
closed_users=[]

protection = False


@app.route("/")
def index():
    return render_template('index.html', len=len(closed_users),closed_users=closed_users)


@app.route("/requestchallenge")
def request_challenge():
    challenge = get_random_challenge()
    
    global protection 

    if protection==True:
        challenge = challenge+'|server'

    user = request.args.get('user', None)
    connection_request[user]=challenge

    return jsonify(
        challenge=challenge
    )

@app.route("/responseOfAChallenge")
def responseOfAChallenge():
    user  = request.args.get('user', None)
    response  = request.args.get('response', None)
    
    file = open('user.key', 'rb')
    key = file.read()
    f = Fernet(key)
    file.close()

    byteresponse = str.encode(response)
    decripted_response = f.decrypt(byteresponse).decode('utf-8')
    challenge = connection_request[user]

    message='NOT AUTHENTICATED'
    if(decripted_response==challenge):
        message='AUTHENTICATED'

    closed_users.append([user,message])
    del connection_request[user]

    return jsonify(
        response = decripted_response,
        challenge = challenge,
        message = message
    )

    
@app.route("/responseToAChallenge")
def responseToAChallenge():
    user = request.args.get('user', None)
    challenge = request.args.get('challenge', None)
    
    global protection
    if protection==True:
        if not '|client' in challenge:
            message='NOT AUTHENTICATED'
            closed_users.append([user,message])
            del connection_request[user]

            return jsonify(
                response = 'CHALLENGED FORMAT UNKNOWN'
            )

    file = open('user.key', 'rb')
    key = file.read()
    f = Fernet(key)
    file.close()

    bytechallenge = str.encode(challenge)
    d = f.encrypt(bytechallenge).decode('utf-8')
    
    return jsonify(
        challenge = challenge,
        response = d
    )


@app.route("/execute_client",methods=["POST"])
def execute_client():
    global protection

    try:
        request.form['check']
        protection = True
    except:
        protection = False

    file = open(r'client.py', 'r').read()
    exec(file)
    protection = False
    return render_template('index.html', len=len(closed_users),closed_users=closed_users)

if __name__ == "__main__":
    app.run()
