#!/bin/sh

set -e

if [ ! -z $1 ] 
then 
    while sleep $1; do
        echo "I'm not away."
    done
else
    while sleep 10; do
        echo "I'm not away."
    done
fi
