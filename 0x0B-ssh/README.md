0x0B SSH


**Learning Objectives**
- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantages of using #!/usr/bin/env bash instead of using /bin/bash


Server - A piece of computer hardware or software that provides functionality for
	other programs or devices, called clients.
	- Servers serve Users and Users use Servers.
	- Servers serve data to clients. The nature of communication between a client
	and server is 'request and response'

SSH - SSH is a secure protocol used as the primary means of connecting to Linux servers remotely.
	- It provides a text-based interface spawning a remote shell.
	- After connecting, all commands you type in your local terminal are sent to the
	  remote server and executed there.
- SSH overview:
	When you connect through SSH, you log in using an account that exists on
	the remote server.
- How SSH works:
	When you connect through SSH, you will be dropped into a shell session, which is a text-
	based interface where you can interact with your server. For the duration of your
	session, any commands you type into your local terminal are sent through an encrypted
	SSH tunnel and executed on your server.
	- For an SSH connection to be established, the remote machine must be running a piece
	  of software called an SSH daemon. The software listens for connections on a specific
	  network port, authenticates connection requests, and spawns the appropriate
	  environment if the user provides the correct credentials
	- The user's computer must have an SSH client.
