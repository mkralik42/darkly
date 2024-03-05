# UNSECURE REDIRECTS

## VULNERABILITY

In the footer, there are three redirect links to social media. Inspecting the Instagram logo, for example, reveals that it queries the backend and redirects to a site.

```html
<li>
  <a
    href="index.php?page=redirect&site=instagram"
    class="icon fa-instagram"
  ></a>
</li>
```

## EXPLOIT

We manipulated the URL from "?page=redirect&site=instagram" to "?page=redirect&site=wikipedia," then clicked on the Instagram logo to obtain the flag.

## INFOS

This vulnerability poses a significant risk as it allows for the modification of redirection to potentially malicious sites. An attacker could execute a phishing scam, leading users to divulge sensitive credentials. One notable example is redirecting to a fraudulent banking site.

## PATCH

To improve the security of redirects and prevent potential exploitation, consider the following measures:

    1. Backend Validation:
      - Implement robust validation checks on the backend to ensure that redirect URLs are thoroughly sanitized.
      - Verify the legitimacy of the redirect URLs against a secure database or an allow list of trusted URLs.

    2. Restrict User Input:
      - Avoid allowing user input for redirect URLs unless the value is valid, appropriate, and explicitly authorized for the user.

    3. Forced Confirmation Page:
      - Enforce a mandatory confirmation page for all redirects, ensuring users are notified that they are leaving your site.
      - Display the destination URL prominently and require users to click a link to confirm their intent before proceeding.

    4. Secure Parameter Handling:
      - When using parameters in redirect URLs, adopt secure handling practices to prevent manipulation by attackers.
      - Avoid passing sensitive information through URL parameters.

    5. Monitoring and Logging:
      - Set up monitoring and logging mechanisms to detect and log suspicious redirect activities. This can help in identifying and responding to potential attacks.

## SOURCES

https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
