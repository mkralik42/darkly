# XXS CROSS SITE SCRIPTING

## VULNERABILITY
On this page, there are user input that is not well protected from XSS.

## EXPLOIT
The feedback page makes you want to inject a script into the inputs (XSS script from OWASP), but it seems that there is a filter that suppress the anything with <> and the comment returns empty.
Strange thing is if you write alert or script, the flag pop up.
Once you land the flag, you will have to restart the machine if you want to try other inputs since the flag wont go away.

## INFOS
Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application.
XSS attacks are serious and can lead to account impersonation, observing user behaviour, loading external content, stealing sensitive data, and more.

## PATCH
Treat all user input as untrusted
Use a filter that remove dangerous keywords, for example, the infamous < script> tag, JavaScript commands, CSS styles, and other dangerous HTML markups
Use escaping/encoding (tell the browser that the data you are sending should be treated as data and should not be interpreted in any other way)
Set the HttpOnly flag

## SOURCES
https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
https://www.acunetix.com/blog/articles/preventing-xss-attacks/
