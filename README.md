# Reflection Attack
This repository contains a toy example of a reflection attack for an authentication method 

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
2. server replies with an R challenge
3. user opens a second connection with the server, this time asking for its authentication by sending it an R challenge.
4. server responds with the hashing of R
5. user lefts the second communication and uses the hashing obtained to respond to the first challenge
