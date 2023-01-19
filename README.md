# Reflection Attack
This repository contains a toy example of a reflection attack for an authentication method 

<div align=center>
 <img src="https://github.com/mariocuomo/reflection-attack/blob/main/images_readme/flask-app.png">
</div>

The web server is developed using python and flask. <br>
To start it execute the following command and visit http://127.0.0.1:5000.

```console
mario@mario-lap:~$ python run.py 

* Serving Flask app "run" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

Think the following situation. <br>
There is a web server that offers a service to authenticated users only.<br>
Authenticate a user means being sure that they are really who they say they are. <br>
There are several methods to authenticate: one of these is the use of a **_pre-shared key_**, a secret initially exchanged between users and servers. Only users who can be authenticated have the pre-shared key. <br>
Users must demonstrate that they know the pre-shared key. It is obvious that they cannot directly exchange the secret with the server: a malicious user could be on the channel and acquire it. <br>

<div align=center>
 <img src="https://github.com/mariocuomo/reflection-attack/blob/main/images_readme/pre-shared-key.png">
</div>

One way is to use a **_challenge-response approach_**. <br>
When a user requests a connection to the server, it replies with a _challenge_: it sends him a string that the user must encrypt using the shared-key and then return it to the server. The server also performs hash in local and checks if it matches with the received one. <br>

<div align=center>
 <img src="https://github.com/mariocuomo/reflection-attack/blob/main/images_readme/challenge-response.png">
</div>

Likewise, the user must also be convinced that he is communicating with the real web server. <br>
The client can also send a challenge-response to the server to authenticate it. <br>

<div align=center>
 <img src="https://github.com/mariocuomo/reflection-attack/blob/main/images_readme/mutual-authentication.png">
</div>


Seems all right, right? <br>
In several mutual authentication protocols the authentication mechanisms are the same for both _user->server_ and _server->user_ authentication. Often the same keys are used to hashing challenges and server authentication can be execute before the one about the user! <br>
The Reflection Attack exploits use all of these vulnerabilities together to break authentication protocol. <br>
The idea is to ask the server to respond to the challenge sent by it previously. <br>

1. user opens a new authentication request with the server
2. server replies with a challenge R
3. user opens a second connection with the server, this time asking for its authentication by sending it a challenge R (the previous one!)
4. server responds with the hashing of R
5. user left the second communication and uses the hashing obtained to respond to the first challenge

<div align=center>
 <img src="https://github.com/mariocuomo/reflection-attack/blob/main/images_readme/reflection-attack.png">
</div>

user can authenticate itself without knowing the key! <br>


How to protect web server from reflection attack?<br>
A very simple method is to associate the mac - Message message authentication Code - to the message. <br>
A second method, which is the one implemented, is to break the symmetry of the requests: the server only responds to challenges of the type ```R+'|client'``` and only offers challenges to users such as ```R+'|server```. <br>
An important insight [here](https://cwe.mitre.org/data/definitions/301.html).

