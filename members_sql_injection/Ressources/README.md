# SQL INJECTION

## VULNERABILITY
In the member section we can access info about the members. Infos about the members means DATABASE. Id goes from 1 to 5, the 5th member is named "Get The Flag".

## EXPLOIT
We just spotted a clue. "1 or 1=1" display all the users. Trying this as always: "1 UNION SELECT table_name, column_name FROM information_schema.columns". Then among all the informations, we control F "members", and then "users" to find that there is 8 categories in users.
After many fails, we used: 1 UNION SELECT countersign, commentaire FROM users, that gave us:
"First name: 5ff9d0165b4f92b14994e5c685cdce28
Surname : Decrypt this password -> then lower all the char. Sh256 on it and it's good !"

## INFOS
SQL injection allows an attacker to interfere with the queries that an application makes to its database.
With this vulnerability, an attacker could read/delete/insert sensitive data from the complete database (involving users' personal information, emails, password, etc).

## PATCH
The client should not be able to supply an input, whitelist input validation is recommended.
An other solution would be to use an ORM that will natively prevent SQL injections.

## SOURCES
https://portswigger.net/web-security/sql-injection



