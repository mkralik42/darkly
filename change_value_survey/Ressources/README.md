# INSECURE DATA VALIDATION

## VULNERABILITY
On the survey page, users can submit votes through an array with a user input. However, there are concerns about the effectiveness of input validation protection. Let's examine the security measures in place for these values.

## EXPLOIT
By inspecting the network traffic after submitting a vote (/?page=survey), we identify the values (subject and value) included in the request body. Right-clicking on the POST request allows us to edit and resend it. By modifying the value to something higher than 10, we were able to obtain the flag. Upon sending it, we checked the response to confirm successful exploitation.

## INFOS
This vulnerability exposes the web application to various threats, including injection attacks, buffer overflows, and more.

## PATCH
To limit this issue, it is essential to implement robust backend controls, ensuring values are thoroughly validated, sanitized, and checked before processing.

## SOURCES
https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html#improper-data-validation
