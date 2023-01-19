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


Seems all right, right?
