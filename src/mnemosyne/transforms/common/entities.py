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
    'MnemosyneHPIncident'
]

"""
DO NOT EDIT:
The following entity is the base entity type from which all your entities will inherit from. This provides you with the
default namespace that all your entities will use for their unique entity type in Maltego. For example, MyMnemosyneEntity will
have an entity type name of mnemosyne.MyMnemosyneEntity. When adding a new entity in Maltego, you will have to specify this
name (mnemosyne.MyMnemosyneEntity) in the 'Unique entity type' field.
"""


class MnemosyneEntity(Entity):
    namespace = 'mnemosyne'


"""
You can specify as many entity fields as you want by just adding an extra @EntityField() decorator to your entities. The
@EntityField() decorator takes the following parameters:
    - name: the name of the field without spaces or special characters except for dots ('.') (required)
    - propname: the name of the object's property used to get and set the value of the field (required, if name contains dots)
    - displayname: the name of the entity as it appears in Maltego (optional)
    - type: the data type of the field (optional, default: EntityFieldType.String)
    - required: whether or not the field's value must be set before sending back the message (optional, default: False)
    - choices: a list of acceptable field values for this field (optional)
    - matchingrule: whether or not the field should be loosely or strictly matched (optional, default: MatchingRule.Strict)
    - decorator: a function that is invoked each and everytime the field's value is set or changed.
TODO: define as many custom fields and entity types as you wish:)
"""

#protocol type
@EntityField(name='mnemosyne.ipv4addr', propname='ipv4addr', displayname='IP')
@EntityField(name='mnemosyne.honeypot', propname='honeypot', displayname='Honeypot')
class MnemosyneHoneypot(MnemosyneEntity):
    #iconurl = 'file://%s' % resource_filename('mnemosyne.resources.images', 'hp_logo.png')
    pass

#protocol type
@EntityField(name='mnemosyne.protocol', propname='protocol', displayname='Protocol')
class MnemosyneProtocol(MnemosyneEntity):
    pass

#Extractions
@EntityField(name='mnemosyne.timestamp', propname='timestamp', displayname='Timestamp', type=EntityFieldType.String)
#Which hash to use as value?
@EntityField(name='mnemosyne.sha512', propname='sha512', displayname='SHA-512', type=EntityFieldType.String)
@EntityField(name='mnemosyne.sha1', propname='sha1', displayname='SHA-1', type=EntityFieldType.String)
@EntityField(name='mnemosyne.md5', propname='md5', displayname='MD5', type=EntityFieldType.String)
@EntityField(name='mnemosyne.hpfeed_id', propname='hpfeed_id', displayname='HPFeed Id', type=EntityFieldType.String)
class MnemosyneExtraction(MnemosyneEntity):
    """
    Uncomment the line below and comment out the pass if you wish to define a ridiculous entity type name like
    'my.fancy.EntityType'
    """
    # name = my.fancy.EntityType

    pass
