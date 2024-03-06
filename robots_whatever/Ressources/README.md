# ROBOTS.TXT

## IDENTIFY THE VULNERABILITY

Recognizing the robots.txt file as a map of the website, we found details indicating the presence of a restricted /whatever directory at http://192.168.56.101/robots.txt.

## EXPLOIT THE VULNERABILITY

Within the vulnerable /whatever directory, we came across an exposed 'htpasswd' file containing sensitive information:

> root:437394baff5aa33daa618be47b75cb49'

Using https://crackstation.net/, we successfully decrypted the password, revealing 'qwerty123@' (md5 hash).
Given the 'root' credentials, we looked for the admin page at http://192.168.56.101/admin. We gained the flag by entering the username 'root' and password 'qwerty123@'.

## INFOS ON THE VULNERABILITY AND ITS RISKS

Robots.txt, known as the robots exclusion protocol, is used to prevent search engine crawlers from accessing certain files on your site. While essential for efficient search indexing, misconfigurations can inadvertently expose directory structures. In this case, the /whatever directory was disclosed, potentially aiding attackers in targeting specific areas.

## PATCH THE VULNERABILITY

To enhance security and limit the risks associated with exposing directory structures through robots.txt, consider the following measures:

1. Disallow Directories:

   Specify disallow rules for directories instead of entire pages. This practice limits potential exposure, requiring attackers to use brute force to discover specific pages.

2. Protect 'htpasswd' with '.htaccess':

   Employ an additional layer of security by safeguarding the 'htpasswd' file with '.htaccess'. 'htpasswd' is commonly used in Apache servers to enforce authentication for specific directories or files.

3. Apply Strong Encryption for Sensitive Directories:

   If certain directories contain highly sensitive information, consider encrypting the content within those directories. This ensures that even if unauthorized access occurs, the data remains unreadable without the appropriate decryption key.

## SOURCES

https://www.searchenginejournal.com/robots-txt-security-risks/289719/
https://httpd.apache.org/docs/2.4/fr/programs/htpasswd.html
