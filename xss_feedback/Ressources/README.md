# STORED XXS (CROSS SITE SCRIPTING)

## IDENTIFY THE VULNERABILITY

The feedback page (http://192.168.56.2/?page=feedback) contains two user inputs for name and message. Upon submission, the data is sent to the server, stored in the database, and displayed on the page. This setup makes it susceptible to XSS attacks, as user inputs are not adequately protected.

## EXPLOIT THE VULNERABILITY

We tried injecting a script into the inputs, but it seems there's a filter blocking anything with '<>' tags, resulting in empty comments. However, we successfully triggered the flag by entering specific keywords like 'script' or 'alert'.

## INFORMATION ON STORED XSS

Cross-site scripting (XSS) is a significant web security vulnerability enabling attackers to compromise user interactions within a vulnerable application. These attacks pose serious risks, ranging from account impersonation and monitoring user behavior to loading external content and stealing sensitive data.

This specific case is a stored XSS attack : the injected script is permanently stored on the server. This stored script is then served to other users accessing the same content, allowing the attacker to impact multiple users. This type of XSS presents a persistent threat as malicious scripts remain on the server, affecting all users who view the compromised content.

## PATCH THE VULNERABILITY

To reduce the risks associated with stored XSS attacks, consider implementing the following security measures:

    1. Input Validation and Filtering:
      - Treat all user input as untrusted.
      - Use a strict filter to remove dangerous keywords, such as the infamous <script> tag, JavaScript commands, CSS styles, and other hazardous HTML markups.

    2. Encode data on output
      - Encode the output to prevent it from being interpreted as active content. Depending on the output context, this might require applying combinations of HTML, URL, JavaScript, and CSS encoding.

    3. Use Appropriate Response Headers:
      - Set the HttpOnly flag for cookies to prevent them from being accessed through JavaScript, reducing the risk of unauthorized access to session information.
      - Implement proper response headers, such as Content-Type and X-Content-Type-Options, to prevent XSS in HTTP responses not intended to contain HTML or JavaScript.

    4. Content Security Policy (CSP):
      - Implement Content Security Policy (CSP) to reduce the severity of any XSS vulnerabilities that may still occur. CSP allows website administrators to define and enforce a set of policies specifying the trusted sources of content that the browser should execute or load.

## SOURCES

https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
https://www.acunetix.com/blog/articles/preventing-xss-attacks/
https://portswigger.net/web-security/cross-site-scripting
