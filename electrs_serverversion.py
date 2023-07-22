import socks
import json
import re

# SOCKS5 Proxy
PROXY_HOST = 'localhost'
PROXY_PORT = 9050

# Electrum Server
ELECTRS_HOST = "umbrel.local"

s = socks.socksocket()

# Make Request
req = { "id": 0, "method": "server.version", "params": [ "0.6", "1.4" ] }
req = json.dumps(req).encode('utf-8') + b'\n'

# RPC
try:
    c = s.connect(("umbrel.local", 50001))
except Exception as e:
    print(e)

s.sendall(req)
res = s.recv(4096)

# Parse Response
res = json.loads(res)
print(res)
