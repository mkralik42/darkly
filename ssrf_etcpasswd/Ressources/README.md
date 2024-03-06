# PATH TRAVERSAL AND SSRF

## IDENTIFY THE VULNERABILITY

Exploring common web application vulnerabilities, we identified gaining access to the /etc/passwd file as a significant threat. So, we will attempt to access it.

## EXPLOIT THE VULNERABILITY

In this context, we attempted to find the path to the /etc/passwd file by using the “dot-dot-slash (../)” method, navigating through directories and requesting the server for the flag. Encouraging pop-ups confirmed that we were on the right track. Ultimately, we obtained the flag using the following path:

> http://192.168.56.2/index.php?page=../../../../../../../etc/passwd

## INFORMATION ON SSRF AND PATH TRAVERSAL

A Server-side Request Forgery (SSRF) vulnerability arises when an attacker manipulates a server-side application, making it send HTTP requests to a specified domain. This vulnerability exposes the server to arbitrary external requests directed by the attacker.

Path traversal attacks (or directory traversal) aim to access files and directories stored outside the web root folder. An attacker gaining such access could obtain sensitive information and execute previously uploaded scripts, leading to potential security breaches.

## PATCH THE VULNERABILITY

Limit SSRF and path traversal vulnerabilities through the following measures:

1. Input Validation:

   - Rigorously sanitize and validate user input.
   - Implement strict controls on input parameters to prevent malicious data.

2. Path Security:

   - Avoid exposing local filesystem paths based on user input.
   - Enforce server-side validation for user-specified paths, excluding restricted characters.

3. Access Controls:

   - Implement strong access controls to restrict server-side requests.
   - Authorize and validate server-side requests to specific domains.

4. Logging and Monitoring:

   - Set up comprehensive logging to track and detect SSRF attempts.
   - Monitor and log suspicious activities related to path traversal.

## SOURCES

https://owasp.org/www-community/attacks/Path_Traversal
https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery
