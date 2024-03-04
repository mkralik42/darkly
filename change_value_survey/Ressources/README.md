# INSUFFICIENT DATA VALIDATION

## VULNERABILITY
In the page survey, there is an array where you can vote with a user input. Let's see if the values are protected.

## EXPLOIT
Click right > inspect > Network > Post /?page=survey > Request, here we can see that there are two values (subject et value). Right click on the POST > Edit and Resend > scroll down to body and change the values. Then send it and check the Response if the page didn't load.

## INFOS
This vulnerability may expose the web application to many situations like injection, attack, buffer overflow, etc.

## PATCH
The values should always be controlled, sanitized and checked in the backend.

## SOURCES
https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html#improper-data-validation
