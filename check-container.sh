#!/bin/sh
set -e

function checkService(){

    rm -rf ./container-result-file
    docker ps -q -f status=exited | cat >> ./container-result-file

    cat ./container-result-file | while read line
    do
        rm -rf ./container-result-file
        echo "   ✘ service failed!"
        return 1
    done

    echo "   ✓ service checked"
    rm -rf ./container-result-file
}

checkService