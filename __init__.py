from modules import app, cbpi
from flask import request, abort

import socket

try:
    from netaddr import IPNetwork, IPAddress
except:
    import os
    os.system('pip install netaddr')
    from netaddr import IPNetwork, IPAddress


ip_address = socket.gethostbyname(socket.gethostname())
split = ip_address.split('.')
local_cidr = "{}.{}.{}.0/24".format(split[0], split[1], split[2])


def getCustomCidrs():
    custom_cidrs = cbpi.get_config_parameter('custom_cidrs', None)
    if custom_cidrs is None:
        cbpi.add_config_parameter(
            "custom_cidrs", "", "text", "Comma seperated cidrs for allowed networks")
        return []
    else:
        if custom_cidrs == "":
            return []
        else:
            return custom_cidrs.encode("UTF-8").split(',')


static_cidr = [
    "127.0.0.1/32",
    local_cidr
]


@app.before_request
def limit_remote_addr():
    custom_cidrs = getCustomCidrs()
    full_cidrs = static_cidr + custom_cidrs
    for address in full_cidrs:
        if IPAddress(request.remote_addr) in IPNetwork(address):
            return

    abort(404)
