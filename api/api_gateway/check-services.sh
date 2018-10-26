#!/bin/bash

red="\033[1;31m"
green="\033[1;32m"
nocolor="\033[0m"

# echo "checking internet connectivity..."
# if [ $(curl --write-out %{http_code} --silent --output /dev/null https://google.com ) == 000 ]
# then
#     echo "${red}not connected with the internet...${nocolor}"
# else
#     echo "${green}connected with the internet...${nocolor}"
# fi

declare -a services=(
                    "http://login-microservice:8000" 
                    "http://product-microservice:8000"
                    "http://order-microservice:8000"
                    )

for s in "${services[@]}"
do
    retries=30
    while [ "$(curl --write-out %{http_code} --silent --output /dev/null ${s})" == "000" ]
    do
        echo "✘ ${s} not connected"
        sleep 1
        echo "retry: $((--retries))"
        if [ $retries == 0 ]
        then
            exit 0;
        fi
    done
    echo " ✓  ${s} connected!"
done