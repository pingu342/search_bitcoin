#!/bin/bash

DATE=`date -u "+%Y/%m/%d %H:%M:%S"`
SEED=`cat -`
PRI=`echo $SEED | openssl dgst --sha256 -binary | xxd -p -c 32`
PUB=`echo -n $PRI | bx ec-to-public`
ADR=`echo -n $PUB | bx ec-to-address`
RES=`echo -n $ADR | ./getaddressbalance.sh $1`
echo "Date    : $DATE"
echo "Seed    : $SEED"
echo "Private : $PRI"
echo "Public  : $PUB"
echo "Address : $ADR"
echo "Balance : $RES"
