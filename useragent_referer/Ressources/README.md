# FORGED REQUEST HEADERS

## VULNERABILITY
Upon clicking on the footer copyright link, we discovered the albatroz page: 'http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f'.Further inspection of the page's comments revealed critical information: 
"You must come from: 'https://www.nsa.gov/' to go to the next step
... 
Let's use this browser: 'ft_bornToSec'. It will help you a lot."

## EXPLOIT THE VULNERABILITY
We formulated a new request to the website on the specified page, manipulating the referer and user-agent headers with forged data. Using curl, we employed the following options:
- The `-e` or `--referer` option to set the referer
- The `-A` or `--user-agent` option to set the user-agent

Curl allows us to specify the referrer on the command line, and to define the browser generating the request. Our goal was to deceive the server into thinking the request originated from the NASA site and was made using a browser named 'ft_bornToSec'.

Here's the complete command we used to retrieve the flag :
curl -A "ft_bornToSec" -e "https://www.nsa.gov/" http://192.168.56.101/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

## INFORMATION ON THE VULNERABILITY AND ITS RISKS
The vulnerability arising from forged request headers poses a significant risk to web applications. The User-Agent and Referer informations are very important, but because they
are easy-to-read strings in plain text, it is easy to be tampered with.
By manipulating the referer and user-agent headers, attackers can deceive a server into believing that a request originates from a trusted source or a specific browser. This manipulation undermines the authenticity of the incoming requests, potentially leading to unauthorized access, data breaches, or other malicious activities. 

## PATCH
To reduce the risks associated with manipulated request headers, it is imperative not to blindly trust the information provided in headers. Web applications should :

    - Validate and Verify Headers: Implement rigorous validation checks for incoming request headers, particularly referer and user-agent.

    - Verify the integrity and authenticity of headers to prevent potential misuse and unauthorized access.

    - Detect Forged Headers: Incorporate mechanisms to detect and block forged headers, adding an extra layer of protection.

## SOURCES
https://everything.curl.dev/http/modify/user-agent
https://everything.curl.dev/http/modify/referer
