# COOKIES BREACH

## IDENTIFY THE VULNERABILITY

While inspecting the site, we checked the cookies stored in the browser's storage through the browser's developer tools. We found a sensitive cookie with the identifier: "I_am_admin" and the value: "68934a3e9455fa72420237eb05902327".

> **Cookie: I_am_admin=68934a3e9455fa72420237eb05902327**

## EXPLOIT THE VULNERABILITY

We decrypted the value associated with the "I_am_admin" cookie. Using Crackstation, we decoded the MD5 hash, revealing the plaintext value "false". Then, we edited the cookie value to "true" and hashed it using Cyberchef with MD5. Finally, to obtain the flag, we reloaded the page.

> **Cookie: I_am_admin=b326b5062b2f0e69046810717534cb09**

## INFORMATION ON COOKIE POISONING

The vulnerability comes from insecure storage and handling of session-related cookies, creating an opportunity for attackers to manipulate authentication states and potentially gain unauthorized access to privileged functionalities. Editing or manipulating the cookie allows attackers to access user data, posing a risk of unauthorized account access and identity theft through cookie poisoning attacks.

## PATCH THE VULNERABILITY

To limit the risks associated with insecure handling of session-related cookies, implement the following measures:

1. Cookie Encryption:

   - Encrypt cookies using a secret key.
   - Implement signed cookies verified by the server.

2. Secure Attribute:
   Utilize the "secure" attribute for cookies, ensuring they are sent only for HTTPS requests.

3. Best Practices:
   - Avoid storing critical information in cookies.
   - Implement secure sessions with encryption, strong passwords, and tokens.
   - Use robust hashing algorithms, avoiding insecure methods like MD5.

## SOURCES

https://www.techtarget.com/searchsecurity/definition/cookie-poisoning#:~:text=By%20editing%20or%20manipulating%20the,or%20to%20steal%20their%20identities.
