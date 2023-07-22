# Install

Use macOS.

Install [Libbitcoin Explorer](https://github.com/libbitcoin/libbitcoin-explorer/tree/version3).

    brew install bx

Clone this repository.

    git clone https://github.com/pingu342/search_bitcoin.git

Install dependent python packages.

    cd search_bitcoin
    pip install pysocks
    pip install pycoin

Find the Electrum Server and set its hostname and port number to ELECTRS_HOST, ELECTRS_PORT in electrs_getaddressbalance.py

# Random Search

    ./random_search.sh NUM

This script generate a password of NUM bytes and hash the password using sha256 as the private key.

Next, generate a P2PKH address from the private key.

Finally, check the balance of P2PKH addresses.

ex. NUM=3

    ./random_search.sh 3 | tee -a random_search.log
    Date    : 2023/07/22 06:07:27
    Input   : Hz4
    Private : 4b23ca7514fffad3ae8e99b5618ff52de8a32b62b251cbc991889416c8c8a92c
    Public  : 0378f310bddb5cbce1c6c8bc4a7e4d7c3d5c13e9acaa8a159535dd06b5c2bef0f9
    Address : 1QCi1GSnYovFdiDEVjArJrPKsb8yueGosj
    Balance : {'id': 0, 'jsonrpc': '2.0', 'result': {'confirmed': 0, 'unconfirmed': 0}}

The input field above will be present the generated password of 3 bytes.

If **confirmed** or **unconfirmed** are not zero, the address have bitcoin.

# Dictionary search

    ./dictionary_search.sh FILE

This script uses the passwords in FILE.

Other things are the same as random_search.sh.

ex. FILE=sample_dictionary

    ./dictionary_search.sh sample_dictionary | tee -a dictionary_search.log
    Date    : 2023/07/22 06:25:57
    Input   : test
    Private : f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2
    Public  : 035ce12eab20cec5c0d6cd5daa85e986b195c9b2da42179b34cec738330e781e7a
    Address : 1M8vC4wsgFJtnsDWmqA34FgZ8JWRPV9nJv
    Balance : {'id': 0, 'jsonrpc': '2.0', 'result': {'confirmed': 0, 'unconfirmed': 0}}

# Check log files

Sum all **confirmed** and **unconfirmed**.

    python check_log.py random_search.log

Check multiple log files at once.

    python check_log.py "`ls *.log`"




