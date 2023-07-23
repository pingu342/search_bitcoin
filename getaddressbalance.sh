#!/bin/bash

ADR=`cat -`
if [ "$1" = "electrs" ]; then
	RES=`echo $ADR | python ./electrs_getaddressbalance.py`
else
	RES=`python offline_getaddressbalance.py $ADR sorted-blockchair_bitcoin_addresses_latest.tsv.splitted-*`
fi
echo $RES
