#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure  # , superuser
from canari.maltego.entities import IPv4Address
from common import msmodule
from common.entities import MnemosyneHoneypot
from pkg_resources import resource_filename

__author__ = 'Johnny Vestergaard'
__copyright__ = 'Copyright 2013, Mnemosyne Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Johnny Vestergaard'
__email__ = 'jkv@unixcluster.dk'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


"""
TODO: set the appropriate configuration parameters for your transform.
TODO: Uncomment the line below if the transform needs to run as super-user
"""
#@superuser


@configure(
    label='To Honeypot Attacks [Mnemosyne]',
    description='Returns honeypot attacks from the specified IP.',
    uuids=['mnemosyne.v1.MnemosyneIPToHoneypotAttack'],
    inputs=[('Mnemosyne', IPv4Address)],
    debug=True
)
def dotransform(request, response):

    ip_addr = request.value
    json_dict = msmodule.query('sessions?source_ip={0}'.format(ip_addr))

    honeypot_sessions = json_dict['sessions']

    #{u'destination_ip': u'xx.yyy.zzz.pp', u'protocol': u'ssh', u'hpfeed_id': u'5140f89909ce454287da8188',
    # u'timestamp': u'2013-03-13T22:07:16.669000', u'source_ip': u'qqqq.azz.xxx.qqq', u'source_port': 23909,
    # u'honeypot': u'beeswarm.hive', u'_id': u'514512de09ce45745ae34b53', u'destination_port': 8022,
    # u'auth_attempts': [{u'login': u'postgres', u'password': u'postgres123'}]}

    count = 0
    for s in honeypot_sessions:
        count += 1
        entity = MnemosyneHoneypot(s['destination_ip'])
        entity.iconurl = 'file://%s' % resource_filename('mnemosyne.resources.images', 'hp_logo.png')
        entity.linklabel = '{0} Attacks'.format(count)
        entity.Honeypot = s['honeypot']
        entity.ipv4addr = 'maltego.IPv4Address'
        response += entity

    return response
