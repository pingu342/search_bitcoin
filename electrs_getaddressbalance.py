import socks
import json
import hashlib
import re
from pycoin.symbols.btc import network

def get_script_hash(addr):
    script = network.parse.address(addr).script()
    return hashlib.sha256(script).digest()[::-1].hex()

# SOCKS5 Proxy
PROXY_HOST = 'localhost'
PROXY_PORT = 9050

# Electrum Server
ELECTRS_HOST = "umbrel.local"
#ELECTRS_HOST = "xxxxxxxx.onion"
ELECTRS_PORT = 50001

# Set Proxy for Tor
s = socks.socksocket()
if re.search(r'\.onion$', ELECTRS_HOST):
    s.set_proxy(socks.SOCKS5, PROXY_HOST, PROXY_PORT)

# Get Address from stdin
addr = input().strip()

# Make Request
script_hash = get_script_hash(addr)
req = { "id": 0, "method": "blockchain.scripthash.get_balance", "params": [script_hash] }
req = json.dumps(req).encode('utf-8') + b'\n'

# RPC
try:
    c = s.connect((ELECTRS_HOST, ELECTRS_PORT))
except Exception as e:
    print(e)

s.sendall(req)
res = s.recv(4096)

# Parse Response
res = json.loads(res)
print(res)

