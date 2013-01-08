#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure  # , superuser
from canari.maltego.entities import IPv4Address
from common import msmodule
from common.entities import MnemosyneHPIncident

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
    label='IP To Honeypot Attacks [Mnemosyne]',
    description='Returns honeypot attacks from the specified IP.',
    uuids=['mnemosyne.v1.MnemosyneIPToHoneypotAttack'],
    inputs=[('Mnemosyne', IPv4Address)],
    debug=True
)
def dotransform(request, response):
    #TODO: not hardcore ip! :-)
    #http://172.30.0.93/api/sessions?source_ip=127.0.0.1

    ip_addr = request.value

    json_dict = msmodule.query('/sessions?source_ip={0}'.format(ip_addr))

    honeypot_sessions = json_dict['sessions']

    for s in honeypot_sessions:
        display = '{0} [{1}]'.format(s['honeypot'].capitalize(), s['protocol'])
        entity = MnemosyneHPIncident(display)
        entity.protocol = s['protocol']
        entity.timestamp = s['timestamp']
        entity.type = s['honeypot']
        if 'destination_ip' in s:
            entity.ipv4add = s['destination_ip']
        response += entity

    return response


def onterminate():
    """
    TODO: Write your cleanup logic below or delete the onterminate function and remove it from the __all__ variable
    """
    pass