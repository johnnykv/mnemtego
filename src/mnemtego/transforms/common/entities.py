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

#Which hash to use as value?
@EntityField(name='mnemtego.content_guess', propname='content_guess', displayname='Content Guess')
@EntityField(name='mnemtego.sha512', propname='sha512', displayname='SHA-512', matchingrule=MatchingRule.Strict)
@EntityField(name='mnemtego.sha1', propname='sha1', displayname='SHA-1', matchingrule=MatchingRule.Strict)
@EntityField(name='mnemtego.md5', propname='md5', displayname='MD5', matchingrule=MatchingRule.Strict)
@EntityField(name='mnemtego.hpfeed_id', propname='hpfeed_id', displayname='HPFeed Id')
class MnemosyneExtraction(MnemosyneEntity):
    pass
