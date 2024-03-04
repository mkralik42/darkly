#ROBOTS.TXT

##HOW WE FOUND THE VULNERABILITY
We know that the robots.txt file can serve as a map of the website. It may shows some interesting directories.

##HOW DID WE EXPLOIT IT
We discovered a wd file unprotect against unauthorized access in /whatever containing a password that we can crack with https://crackstation.net/ : qwerty123@. We tested IP/login, IP/signin, IP/admin, the last one led us to the flag, using username=root & password=qwerty123@.

##INFOS ON THE VULNERABILITY AND WHY IT IS DANGEROUS
Robots.txt is known as the robots exclusion protocol, it is used to prevent search engine crawlers from accessing certain files on your site.

##PATCH
You should disallow directories instead of complete page, that way an attacker could still find the page but would have to use brute force. You could protect the htpasswd with a hotaccess. Htpasswd is used in an Apache server to guarantee authentication to specific directories or files. It can be used in conjunction with a .htaccess.

##SOURCES
https://www.searchenginejournal.com/robots-txt-security-risks/289719/
https://httpd.apache.org/docs/2.4/fr/programs/htpasswd.html
