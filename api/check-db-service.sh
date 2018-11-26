#!/bin/bash
set -e

retries=20

while ! pg_isready -h db > /dev/null 2> /dev/null; do
    
    echo "retry: $((--retries))"
    sleep 1
    
    if [ $retries == 0 ]
    then
        echo "✘ database not connected"
        exit 1;
    fi
done

echo "  ✓  database connected!"
