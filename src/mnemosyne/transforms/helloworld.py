#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import MyMnemosyneEntity

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

# Uncomment the line below if the transform needs to run as super-user
#@superuser
"""
The @configure decorator tells mtginstall how to install the transform in Maltego. It takes the following parameters:
    - label:        the name of the transform as it appears in the Maltego UI transform selection menu
    - description:  a short description of the transform
    - uuids:        a list of unique transform IDs, one per input type. The order of this list must match that of the 
                    inputs parameter. Make sure you account for entity type inheritance in Maltego. For example, if you
                    choose a DNSName entity type as your input type you do not need to specify it again for MXRecord, 
                    NSRecord, etc.
    - inputs:       a list of tuples where the first item is the name of the transform set the transform should be part
                    of, and the second item is the input entity type.
    - debug:        Whether or not the debugging window should appear in Maltego's UI when running the transform.
TODO: set the appropriate configuration parameters for your transform.
"""
@configure(
    label='To MyMnemosyneEntity [Hello World]',
    description='Returns a MyMnemosyneEntity entity with the phrase "Hello Word!"',
    uuids=[ 'mnemosyne.v2.MyMnemosyneEntityToPhrase_HelloWorld' ],
    inputs=[ ( 'Mnemosyne', Person ) ],
    debug=True
)
def dotransform(request, response):
    """
    The dotransform function is our transform's entry point. The request object has the following properties:
        - value:    a string containing the value of the input entity.
        - fields:   a dictionary of entity field names and their respective values of the input entity.
        - params:   any additional command-line arguments to be passed to the transform.
    TODO: write your data mining logic below.
    """

    # Report transform progress
    progress(50)
    # Send a debugging message to the Maltego UI console
    debug('This was pointless!')

    # Create MyMnemosyneEntity entity with value set to 'Hello <request.value>!'
    e = MyMnemosyneEntity('Hello %s!' % request.value)
    # Setting field values on the entity
    e.field1 = 2
    e.fieldN = 'test'
    # Update progress
    progress(100)

    # Add entity to response object
    response += e

    # Return response for visualization
    return response


"""
Called if transform interrupted. It's presence is optional; you can remove this function if you don't need to do any
resource clean up.

TODO: Write your cleanup logic below or delete the onterminate function and remove it from the __all__ variable 
"""
def onterminate():
    debug('Caught signal... exiting.')
    exit(0)