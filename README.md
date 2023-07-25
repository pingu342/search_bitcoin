# Install

To check Bitcoin balance, we need an Electrum server.

Alternatively, download a list of Bitcoin addresses and balances in advance. Then we don't need an Electrum server. [see here](https://github.com/pingu342/search_bitcoin/edit/main/README.md#obtaining-a-list-of-bitcoin-addresses)

- macOS user
  
    Install [Libbitcoin Explorer](https://github.com/libbitcoin/libbitcoin-explorer/tree/version3).

        brew install bx
  
    Install pwgen.
    
        brew install pwgen
    
    Install dependent python packages.
    
        pip install pysocks
        pip install pycoin
    
    Clone this repository.
    
        git clone https://github.com/pingu342/search_bitcoin.git
        cd search_bitcoin
        
    Set the Electrum Server to `ELECTRS_HOST`, `ELECTRS_PORT` in electrs_getaddressbalance.py
    
    Perform a random search.

        ./random_search.sh 1 electrs

- Docker user

    Run the ubuntu:20.04 Docker image.
  
        docker pull ubuntu:20.04
        docker run --name test -itd ubuntu:20.04
        docker exec -it test /bin/bash

    Install build tools for building [Libbitcoin Explorer](https://github.com/libbitcoin/libbitcoin-explorer/tree/version3) on ubuntu.

        apt update
        apt upgrade
        apt install g++
        apt install clang-11
        update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-11 50
        update-alternatives --install /usr/bin/clang clang /usr/bin/clang-11 50
        apt install build-essential autoconf automake libtool pkg-config git wget

    Build Libbitcoin on ubuntu.
  
        cd ~/
        git clone https://github.com/libbitcoin/libbitcoin-explorer.git
        cd libbitcoin-explorer
        git checkout version3
        ./install.sh --with-icu --build-icu --build-boost --build-zmq
        bx

    Remove unnecessary items to reduce ubuntu storage space.
  
        cd ..
        rm -rf libbitcoin-explorer
        apt remove build-essential autoconf automake libtool pkg-config
        apt remove g++ clang-11
        apt autoremove
        exit

    Create a Docker image from a container with Libbitcoin installed.
  
        docker stop test
        docker commit test ubuntu_libbitcoin
        docker image ls
        docker container rm test

    Try to run the Docker image and run the bx command.

        docker run --name test -itd ubuntu_libbitcoin
        docker exec -it test /bin/bash
        bx
        exit
        docker container rm test

    Create a volume and container to run search_bitcoin.

        docker volume create ubuntu_libbitcoin_vol
        docker run -v ubuntu_libbitcoin_vol:/root/data --add-host=<hostname>:<ipaddr> --name test -itd ubuntu_libbitcoin

    For `hostname` and `ipaddr`, specify the Docker host's.  These are used when Electrum Server runs on a Docker host.
  
    Run the container and install search_bitcoin and dependencies.

        docker exec -it test /bin/bash
        apt install python3 python3-pip pwgen vim
        update-alternatives --install /usr/bin/python python /usr/bin/python3 1
        pip install pysocks pycoin
        cd ~/data
        git clone https://github.com/pingu342/search_bitcoin
        cd search_bitcoin/

    Set the Electrum Server to `ELECTRS_HOST`, `ELECTRS_PORT` in electrs_getaddressbalance.py

    Perform a random search.

        ./random_search.sh 1 electrs


# Obtaining a list of Bitcoin addresses

Where to obtain : https://gz.blockchair.com/bitcoin/addresses/

Download and unzip

    wget https://gz.blockchair.com/bitcoin/addresses/blockchair_bitcoin_addresses_latest.tsv.gz
    gunzip blockchair_bitcoin_addresses_latest.tsv.gz

Sort the list and then split it. (It takes time)

    ./split_addresses.sh blockchair_bitcoin_addresses_latest.tsv

Count the number of addresses.

    python count_address.py sorted-blockchair_bitcoin_addresses_latest.tsv.splitted-*

ex.

    p2pkh: 22681435 / 48543080 (46.7 %)
    p2sh : 9004736 / 48543080 (18.5 %)
    p2w  : 16009440 / 48543080 (33.0 %)
    other: 847469 / 48543080 (1.7 %)

# Check the balance of the bitcoin address

When using a Electrum Server.

    echo -n ADDRESS | ./getaddressbalance.sh electrs

When using a bitcoin address list.

    echo -n ADDRESS | ./getaddressbalance.sh

# Check the balance of the private key generated from the seed

When using a bitcoin address list.

    echo -n SEED | ./getkeybalance.sh electrs

When using a bitcoin address list.

    echo -n SEED | ./getkeybalance.sh

    
# Random Search

Generate a NUM character seed, hash it using sha256, and use it as private key.

Next, generate a P2PKH address from a private key.

Finally, check the balance of P2PKH address.

When using a Electrum Server.

    ./random_search.sh NUM electrs

When using a bitcoin address list.

    ./random_search.sh NUM

ex. NUM=3

    ./random_search.sh 3 | tee -a random_search.log
    Date    : 2023/07/22 06:07:27
    Seed    : Hz4
    Private : 4b23ca7514fffad3ae8e99b5618ff52de8a32b62b251cbc991889416c8c8a92c
    Public  : 0378f310bddb5cbce1c6c8bc4a7e4d7c3d5c13e9acaa8a159535dd06b5c2bef0f9
    Address : 1QCi1GSnYovFdiDEVjArJrPKsb8yueGosj
    Balance : 0

The Seed field above shows the generated 3-character seed.

If Balance field is not zero, the address have bitcoin.

# Dictionary Search

Use the seed written in FILE.　Otherwise, it is the same as the random search above.

When using a Electrum Server.

    ./dictionary_search.sh FILE electrs

When using a bitcoin address list.

    ./dictionary_search.sh FILE

ex. FILE=sample_dictionary

    ./dictionary_search.sh sample_dictionary | tee -a dictionary_search.log
    Date    : 2023/07/22 06:25:57
    Seed    : test
    Private : f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2
    Public  : 035ce12eab20cec5c0d6cd5daa85e986b195c9b2da42179b34cec738330e781e7a
    Address : 1M8vC4wsgFJtnsDWmqA34FgZ8JWRPV9nJv
    Balance : 0

# Check log files

This script sums all balance in log.

    python check_log.py random_search.log

If you want to check multiple log files at once.

    python check_log.py *.log




