#PATH TRAVERSAL

##VULNERABILITY
Looking at famous web application vulnerability, we found that getting access to the /etc/passwd file is one of them.

##EXPLOIT
In this scenario, we tried to find the path to the file by using the "dot dot slash method", meaning we moved directory to directory and asking the server for the flag.
We knew we were looking in the right direction when the pop ups encourages us.

##INFOS
A Server-side Request Forgery (SSRF) vulnerability occurs when an attacker manipulates a server-side application into making HTTP requests to a domain of their choice. This vulnerability exposes the server to arbitrary external requests directed by the attacker.
A path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder.
An attacker could have access to sensitive information and execute previously uploaded script for example.

##PATCH
You should not have a path to local filesystem with user supplied input or there should be a validation from the server of the path sent by the user. We might exclude some characters like ".." from paths. Limiting the access only to the file present in the page directory.

##SOURCES
https://owasp.org/www-community/attacks/Path_Traversal
https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery
