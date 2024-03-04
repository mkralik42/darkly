# COOKIES BREACH

## VULNERABILITY
While inspecting the site, we checked the cookies in Storage from Inspect. We found this sensitive cookie : "I_am_admin:"68934a3e9455fa72420237eb05902327"

## EXPLOIT
We decrypted the value associated with the "I am admin". Using Crackstation, we translated the value using md5: false. We edited the value with “true” hashed with Cyberchef in md5. To get the flag, we reloaded the page.

## INFOS
By editing or manipulating the cookie, the attacker can gain access to the user data stored in the cookie. Cookie poisoning attacks are dangerous because they enable attackers to use the data stored inside cookies to gain unauthorized access to users' accounts or to steal their identities.

In this configuration, we could obtain the admin rights just by editing the cookie section. First, we do not advise putting critical information in Cookies. We would recommend using a proper session with connection, password and token. Moreover use a secure algorithm for hashing, md5 are insecure and very easy to crack.

## PATCH
You could encrypt the cookie with an secret key, or use a signed cookie (sign by the server), or even use the "secure" attribute (the cookie will only be send for HTTPS requests).

## SOURCES
https://www.techtarget.com/searchsecurity/definition/cookie-poisoning#:~:text=By%20editing%20or%20manipulating%20the,or%20to%20steal%20their%20identities.
