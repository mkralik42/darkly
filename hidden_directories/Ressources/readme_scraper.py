#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import Fore, Style
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import signal
import readchar

# If needed, customize the IP address in the URL 
URL = "http://192.168.56.101/.hidden/"
readme_count: int = 0

#############################################################################
#                                   UTILS                                   #
#############################################################################

# Create a requests session with retry configuration
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)

# Ctrl-C Handler
def ctrl_c_handler(signum: int, frame) -> None:
    msg = "\nCtrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        # clear the printed line
        print(" " * len(msg), end="", flush=True)
        print("    ", end="\r", flush=True)

# Register the handler function for SIGINT (Ctrl-C)
signal.signal(signal.SIGINT, ctrl_c_handler)

def print_colored_message(message, color=Fore.LIGHTWHITE_EX, end='\n', flush=False):
    print(color + message + Style.RESET_ALL, end=end, flush=flush)

def get_link_elements(url: str) -> set:
    try:
        # Send a GET request to the URL with a timeout
        response = session.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all img elements
            link_elements = soup.find_all('a')
            return link_elements
        else:
            print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def clean_url(base_url: str, path: str) -> str:
    parse_result = urlparse(path)

    # Remove fragment identifiers
    parse_result = parse_result._replace(fragment='')

    # Resolve relative URLs to absolute URLs
    absolute_url = urljoin(base_url, parse_result.geturl())

    # Check if it's not an external link
    if base_url in absolute_url:
        return absolute_url

    return ''

#############################################################################
#                                README SEARCH                              #
#############################################################################

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
            print_colored_message(f'{readme_content}', Fore.BLUE, end='\r', flush=True)

            if "flag" in readme_content.lower():
                # Save the content to a file in append mode in the current directory
                with open(output_file, 'a', encoding='utf-8') as file:
                    file.write(f"URL: {url}\n")
                    file.write(readme_content)
                    print_colored_message(f"\nMatching README file:")
                    print_colored_message(f"{url}", Fore.GREEN)
                    print_colored_message(f"The content has been copied to the '{output_file}' file")
                    return True

        else:
            print_colored_message(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}", Fore.RED)
        return False

    except Exception as e:
        print_colored_message(f"Error: {e}", Fore.RED)

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
            print_colored_message(f"Error: {e}", Fore.RED)

#############################################################################
#                                   MAIN                                    #
#############################################################################

def main():
    visited_urls = set()
    print_colored_message(f"\nExplore all subdirectories under the URL : {URL}")
    print_colored_message(f"  ⮕ to locate and read all README files", Fore.WHITE)
    print_colored_message("  ⮕ and search for the occurrence of the word 'flag'\n", Fore.WHITE)
    recursive_readme_search(URL, visited_urls, depth=4)
    print(f'\033[K\nVisited urls: {len(visited_urls)}')
    print(f'Total Readme: {readme_count}')

if __name__ == "__main__":
    main()
