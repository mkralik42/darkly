# REFLECTED XXS (CROSS SITE SCRIPTING)

## VULNERABILITY

On the main page, we noticed that the 'nsa_prism' image is clickable and leads to the URL: http://192.168.56.101/?page=media&src=nsa.
This functionality provides an opportunity for injecting code after the 'src=' parameter. The page is susceptible to reflected XSS, reflecting user input without adequate validation or escaping.

## EXPLOIT

We tested various XSS payload scripts, such as the following:

```html
< script>alert("XSS");</ script>
```

After additional testing, we acknowledged the necessity to encode the data in base64 using the following format:

```html
data:[<mediatype>][;base64],<data></data></mediatype>
```

As a result, we modified the URL by integrating the encoded script in base64, as shown below:
http://192.168.56.2/?page=media&src=nsa&src=data:text/html;base64,PCBzY3JpcHQ+YWxlcnQoIlhTUyIpOzwvIHNjcmlwdD4=

## INFOS

Cross-site scripting (XSS) represents a significant web security vulnerability that exposes users to various risks within a susceptible application. XSS attacks, if successfully exploited, can result in severe consequences such as account impersonation, monitoring user behavior, loading external content, and stealing sensitive data.

In this specific case, the vulnerability presents as a reflected XSS attack, where an injected script reflects off the web server, impacting a single user without persistent storage. The attack occurs by injecting scripts through the "src" parameter in a URL. These injected scripts are reflected back to users when they interact with the manipulated URL. This process creates potential threats, including the risk of session hijacking, unauthorized access, and extraction of sensitive data.

## PATCH

To reduce the risks associated with stored XSS attacks, consider implementing the following security measures:

    1. Input Validation and Filtering:
      - Treat all user input as untrusted.
      - Use a strict filter to remove dangerous keywords, such as the infamous <script> tag, JavaScript commands, CSS styles, and other hazardous HTML markups.

    2. Encode data on output
      - Encode the output to prevent it from being interpreted as active content. Depending on the output context, this might require applying combinations of HTML, URL, JavaScript, and CSS encoding.

    3. Use Appropriate Response Headers:
      - Set the HttpOnly flag for cookies to prevent them from being accessed through JavaScript, reducing the risk of unauthorized access to session information.
      - Implement proper response headers, such as Content-Type and X-Content-Type-Options, to prevent XSS in HTTP responses not intended to contain HTML or JavaScript.

    4. Content Security Policy (CSP):
      - Implement Content Security Policy (CSP) as a last line of defense to reduce the severity of any XSS vulnerabilities that may still occur.

## SOURCES

https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs
https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
https://www.acunetix.com/blog/articles/preventing-xss-attacks/
https://portswigger.net/web-security/cross-site-scripting/reflected
