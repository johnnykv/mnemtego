#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure  # , superuser
from canari.maltego.entities import URL
from common import msmodule
from common.entities import MnemosyneExtraction
import re

__author__ = ''
__copyright__ = 'Copyright 2013,  Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = ''
__email__ = ''
__status__ = 'Development'

__all__ = [
    'dotransform',
    ]


@configure(
    label='Extraction to URL [Mnemosyne]',
    description='Returns URLs from which this file has been extracted.',
    uuids=['mnemtego.v1.ExtractionToURL'],
    inputs=[('Mnemtego', MnemosyneExtraction)],
    debug=True
)
def dotransform(request, response):

    if 'mnemtego.md5' in request.fields:
        for item in get_urls(request.fields['mnemtego.md5']):
            response += item

    return response

def get_urls(hash):
    result = msmodule.query('urls?hash={0}'.format(hash))['urls']
    for item in result:
        u = URL(item['url'])
        u.url = item['url']
        yield u
