#CLIENT-MODIFIABLE VALUE

##VULNERABILITY

When attempting to use the "I forgot my password" link, we noticed the absence of a user input field for entering our email in the password recovery form. After inspecting the submit button, we discovered a hidden input containing the webmaster's address.

##EXPLOIT

To obtain the flag, we removed the "type=hidden" attribute from the code, making the email field visible. Then, we changed the address and submitted the form.

##INFOS

Hidden Field Manipulation is a type of web application attack that involves modifying the values of hidden fields in a form. Hidden fields are used in HTML forms to store data that is not meant to be seen or modified by users, such as session IDs or other sensitive information.

In HFM attacks, an attacker can modify the values of these hidden fields to bypass security measures, gain unauthorized access, or perform other malicious actions. This can be accomplished by manipulating the HTML code of the form, using automated tools to modify the fields, or exploiting vulnerabilities in the server-side code that processes the form data.

##PATCH

- Server-Side Validation: Strengthen the validation of user inputs on the server side, ensuring that all data submitted adheres to predefined criteria and eliminating the risk of malicious manipulation.

- Avoid pre-filling the webmaster's email address by default on the client side. Instead, securely store this information on the server to prevent potential exposure or manipulation by clients.

##SOURCES

https://cqr.company/web-vulnerabilities/hidden-field-manipulation/
