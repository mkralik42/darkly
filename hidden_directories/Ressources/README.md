# README SEARCH IN HIDDEN DIRECTORIES

## IDENTIFY THE VULNERABILITY

After exploring the robots.txt file, we uncovered the existence of the /.hidden directory, a complex structure with numerous directories, sub-directories, and README files. The intentional complexity seemed designed to obscure the location of the flag

## EXPLOIT THE VULNERABILITY

To navigate through this intricate maze quickly, we developed a Python script for recursive scraping. Using BeautifulSoup, a Python package for parsing HTML and XML documents, we methodically located and read all the README files. Our objective was to identify the presence of the keyword 'flag' within each README.
Finally, we found it on the 4th level of the directory structure, in the file /.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README.

```python
def download_readme(url: str, output_file: str = 'output_readme.txt') -> bool:
    try:
        # Send a GET request to the URL
        response = session.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Use UTF-8 encoding if response.encoding is None
            encoding = response.encoding if response.encoding else 'utf-8'
            # Decode the content manually using the determined or default encoding
            readme_content = response.content.decode(encoding)
            readme_content = readme_content.replace("\n", "")

            if "flag" in readme_content.lower():
                # Save the content to a file in append mode in the current directory
                with open(output_file, 'a', encoding='utf-8') as file:
                    file.write(f"URL: {url}\n")
                    file.write(readme_content)
                    return True

        return False

    except Exception as e:
        print(f"Error: {e}")

def recursive_readme_search(url: str, visited_urls: set, depth: int = 10):
    global readme_count
    if depth == 0 or not url:
        return

    if url in visited_urls:
        return
    else:
        visited_urls.add(url)

    link_elements = get_link_elements(url)
    if link_elements:
        try:
            # Iterate through each link
            for index, link in enumerate(link_elements):
                link_url = link.get('href')
                # Ensure that the base URL has a trailing slash
                url_with_slash = url if url.endswith('/') else url + '/'
                # Join the base URL and the relative URL
                absolute_url = clean_url(url_with_slash, link_url)

                # Check if the link is a README file
                if link_url.endswith("README"):
                    readme_count += 1
                    flag_found = download_readme(absolute_url)
                    if (flag_found == True):
                        return
                else:
                    # Recursively call the function for sub-routes with reduced depth
                    recursive_readme_search(absolute_url, visited_urls, depth=depth - 1)

        except Exception as e:
            print(f"Error: {e}")
```

## INFORMATION ON HIDDEN DIRECTORIES

The utilization of hidden directories, as discovered through the robots.txt file, introduces potential security risks and underscores the importance of proper access controls. While hidden directories aim to obscure specific paths within a web application, their inclusion in the robots.txt file inadvertently discloses their existence. This exposure, combined with the lack of stringent access controls, may lead to unauthorized access to sensitive files contained within these hidden directories.

## PATCH THE VULNERABILITY

To conceal a sensitive file:

- Restrict access to admin privileges :
  Limit file access to privileged accounts, reducing the risk of unauthorized viewing or modification.

- Implement encryption measures :
  Employ encryption techniques to secure the file's contents, ensuring that even if accessed, the information remains unintelligible to unauthorized users.

## SOURCES

https://oxylabs.io/blog/beautiful-soup-parsing-tutorial
