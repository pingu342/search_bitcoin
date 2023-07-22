#!/bin/bash

DATE=`date -u "+%Y/%m/%d %H:%M:%S"`
INPUT=`cat -`
echo "Date    : $DATE"
echo "Input   : $INPUT"
PRI=`echo $INPUT | openssl dgst --sha256 -binary | xxd -p -c 32`
echo "Private : $PRI"
PUB=`echo -n $PRI | bx ec-to-public`
echo "Public  : $PUB"
ADR=`echo -n $PUB | bx ec-to-address`
echo "Address : $ADR"
RES=`echo $ADR | python ./electrs_getaddressbalance.py`
echo "Balance : $RES"
