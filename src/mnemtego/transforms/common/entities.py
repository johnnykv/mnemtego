#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule
from canari.maltego.entities import IPv4Address


__author__ = 'Johnny Vestergaard'
__copyright__ = 'Copyright 2013, Mnemosyne Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Johnny Vestergaard'
__email__ = 'jkv@unixcluster.dk'
__status__ = 'Development'

__all__ = [
    'MnemosyneEntity',
    'MnemosyneHoneypot',
    'MnemosyneExtraction',
]


class MnemosyneEntity(Entity):
    namespace = 'mnemtego'

@EntityField(name='mnemtego.ipv4addr', propname='ipv4addr', displayname='IP')
@EntityField(name='mnemtego.honeypot', propname='honeypot', displayname='Honeypot')
class MnemosyneHoneypot(MnemosyneEntity):
    pass

#protocol type
@EntityField(name='mnemtego.protocol', propname='protocol', displayname='Protocol')
class MnemosyneProtocol(MnemosyneEntity):
    pass

#Extractions
@EntityField(name='mnemtego.timestamp', propname='timestamp', displayname='Timestamp', type=EntityFieldType.String)
#Which hash to use as value?
@EntityField(name='mnemtego.sha512', propname='sha512', displayname='SHA-512', type=EntityFieldType.String)
@EntityField(name='mnemtego.sha1', propname='sha1', displayname='SHA-1', type=EntityFieldType.String)
@EntityField(name='mnemtego.md5', propname='md5', displayname='MD5', type=EntityFieldType.String)
@EntityField(name='mnemtego.hpfeed_id', propname='hpfeed_id', displayname='HPFeed Id', type=EntityFieldType.String)
class MnemosyneExtraction(MnemosyneEntity):
    pass
