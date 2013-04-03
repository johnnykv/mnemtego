#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure  # , superuser
from canari.maltego.entities import IPv4Address
from common.entities import MnemosyneProtocol
from common import msmodule


__author__ = 'Johnny Vestergaard'
__copyright__ = 'Copyright 2013, Mnemosyne Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Johnny Vestergaard'
__email__ = 'jkv@unixcluster.dk'
__status__ = 'Development'

__all__ = [
    'dotransform',
    'onterminate'
]


"""
TODO: set the appropriate configuration parameters for your transform.
TODO: Uncomment the line below if the transform needs to run as super-user
"""
#@superuser


@configure(
    label='To Protocols Attacked [Mnemosyne]',
    description='Returns the types of protocols this IP has attacked.',
    uuids=['mnemtego.v1.IPToAttackedProtocol'],
    inputs=[('Mnemtego', IPv4Address)],
    debug=True
)
def dotransform(request, response):

    ip_addr = request.value
    json_dict = msmodule.query('sessions?source_ip={0}&limit=10000'.format(ip_addr))

    sessions = json_dict['sessions']

    #{u'destination_ip': u'xx.yyy.zzz.pp', u'protocol': u'ssh', u'hpfeed_id': u'5140f89909ce454287da8188',
    # u'timestamp': u'2013-03-13T22:07:16.669000', u'source_ip': u'qqqq.azz.xxx.qqq', u'source_port': 23909,
    # u'honeypot': u'beeswarm.hive', u'_id': u'514512de09ce45745ae34b53', u'destination_port': 8022,
    # u'auth_attempts': [{u'login': u'postgres', u'password': u'postgres123'}]}

    protocols = {}
    for s in sessions:
        if s['protocol'] in protocols:
            protocols[s['protocol']] += 1
        else:
            protocols[s['protocol']] = 1

    for protocol, count in protocols.items():
        entity = MnemosyneProtocol(protocol)
        entity.linklabel = '{0} Activities'.format(count)
        response += entity

    return response


def onterminate():
    """
    TODO: Write your cleanup logic below or delete the onterminate function and remove it from the __all__ variable
    """
    pass