#XXS CROSS SITE SCRIPTING

##VULNERABILITY
One of the image is clickable and lead to the page: http://192.168.56.101/?page=media&src=nsa. This allows us to add some injection after the src=.

##EXPLOIT
After testing a few from the xxs payload list that don't capture the flag, we realised that we need to encode a script "< script>alert(2);</ script>" in base64.
Modify the url with the encode script in base64  > src=data:text/html;base64,PHNjcmlwdD5hbGVydCgyKTs8L3NjcmlwdD4=

##INFOS
Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application.
XSS attacks are serious and can lead to account impersonation, observing user behaviour, loading external content, stealing sensitive data, and more.

##PATCH
Treat all user input as untrusted
Use a filter that remove dangerous keywords, for example, the infamous < script> tag, JavaScript commands, CSS styles, and other dangerous HTML markups
Use escaping/encoding (tell the browser that the data you are sending should be treated as data and should not be interpreted in any other way)
Set the HttpOnly flag

##SOURCES
https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
https://www.acunetix.com/blog/articles/preventing-xss-attacks/
