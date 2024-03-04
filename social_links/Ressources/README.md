# INVALID REDIRECTS

## VULNERABILITY
In the footer, there is 3 redirects to social media. Inspecting the instagram logo for example, show that it queries the backend and redirect to a site.

## EXPLOIT
We can edit that part "redirect&site=wikipedia", then click on the instagram logo to get the flag.

## INFOS
It is dangerous since we could edit the redirection to a malicious site. An attacker may successfully launch a phishing scam and steal user credentials (one of the best example would be to redirect to a fake bank site).

## PATCH
We should check with the backend if it is sanitized or in the database or in an allow list (trusted URLs). You should not allow user input unless the value is valid, appropriate and authorized for the user. We would advice forcing all redirects to first go through a page notifying users that they are going off of your site, with the destination clearly displayed, and have them click a link to confirm.

## SOURCES
https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
