# BRUTE FORCE ATTACK ON SIGN-IN PAGE

## HOW WE IDENTIFIED THE VULNERABILITY
Upon examination, we discovered that the login page allowed an unlimited number of login attempts, and the authentication process was handled through a GET request.

## HOW THE VULNERABILITY WAS EXPLOITED
We executed a brute force attack by repeatedly attempting unauthorized logins using a Python script and a list of commonly used passwords.

## INFORMATION ON THE VULNERABILITY AND ITS RISKS
Brute force is a hacking technique used for guessing the user by trying various possible login credentials. Brute-force involves trying thousands of login credentials repeatedly in a short time span until the attacker succeeds.
In regards to authentication, when no password policy is in place an attacker can use lists of common username and passwords to brute force a username or password field until successful authentication.

## PATCH
To mitigate the risks associated with brute force attacks, consider the following measures:

    1. Switch to POST Request: Prefer using a POST request for login instead of a GET request. This ensures that credentials are sent in the HTTP message body rather than the URL.

    2. Implement Password Complexity:
        - Mix uppercase and lowercase letters.
        - Use alphanumeric combinations.
        - Incorporate special characters for added security.

    3. Limit Login Attempts:
        - Restrict the number of login attempts.
        - Implement IP blocking for repeated failures.
        - Notify users and block accounts after a certain number of unsuccessful attempts.

    4. Require Multi-Factor Authentication (MFA):
        - Enforce the use of two-factor authentication (2FA).
        - 2FA adds an extra layer of security by requiring users to provide two different authentication factors.

    5. Utilize CAPTCHA:
        Implement CAPTCHA to differentiate between human and automated login attempts.

    6. Deploy a Web Application Firewall (WAF):
        Use a WAF to filter and monitor HTTP traffic, providing an additional layer of protection.

    7. Introduce Time Delay:
        Implement time delays between login attempts to slow down brute force attacks.

Implementing these security measures collectively strengthens the defense of the sign-in page against brute force attacks.

## SOURCES
https://www.getastra.com/blog/cms/prevent-brute-force-attack-in-php/

