#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure  # , superuser
from canari.maltego.entities import URL
from canari.maltego.entities import Domain
from common import msmodule
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
    'dotransform'
]


@configure(
    label='Domain to URL [Mnemosyne]',
    description='Returns URLs extracted with automated tools from The Honeynet Project.',
    uuids=['mnemtego.v1.DomainToURL'],
    inputs=[('Mnemtego', Domain)],
    debug=True
)
def dotransform(request, response):

    url = request.value
    regex = '.*{0}(/|:)'.format(re.escape(url))

    json_dict = msmodule.query('urls?url_regex={0}'.format(regex))
    urls = json_dict['urls']
    
    for item in urls:
        u = URL(item['url'])
        u.url = item['url']
        response += u

    return response
