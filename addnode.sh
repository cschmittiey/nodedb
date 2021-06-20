#!/bin/bash

NODEFILE=nodes

if [ "$#" -ne 2 ]; then
    echo -e "Usage:\n\t./addnode.sh IPv6 name [name] ..."
    exit 1
fi

if grep --quiet $1 $NODEFILE; then
    echo "Node IP is already on the list, please edit manually"
    exit 1
fi

echo "$@" >> $NODEFILE

sort $NODEFILE -o $NODEFILE
