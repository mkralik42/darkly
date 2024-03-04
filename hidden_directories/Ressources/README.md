#README SEARCH IN HIDDEN DIRECTORIES

##HOW WE FOUND THE VULNERABILITY
After exploring the robots.txt file, we uncovered the existence of the /.hidden directory, a complex structure with numerous directories, sub-directories, and README files. The intentional complexity seemed designed to obscure the location of the flag

##EXPLOIT
To navigate through this intricate maze quickly, we developed a Python script for recursive scraping. USing BeautifulSoup, a Python package for parsing HTML and XML documents, we methodically located and read all the README files. Our objective was to identify the presence of the keyword 'flag' within each README.

##INFORMATION ON THE VULNERABILITY AND ITS RISKS
The utilization of hidden directories, as discovered through the robots.txt file, introduces potential security risks and underscores the importance of proper access controls. While hidden directories aim to obscure specific paths within a web application, their inclusion in the robots.txt file inadvertently discloses their existence. This exposure, combined with the lack of stringent access controls, may lead to unauthorized access to sensitive files contained within these hidden directories. 

##PATCH
To conceal a sensitive file:
    - Restrict access to admin privileges:
        Limit file access to privileged accounts, reducing the risk of unauthorized viewing or modification.
    - Implement encryption measures:
        Employ encryption techniques to secure the file's contents, ensuring that even if accessed, the information remains unintelligible to unauthorized users.

##SOURCES

