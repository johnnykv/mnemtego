#!/usr/bin/env python

import re

from canari.framework import configure
from canari.maltego.entities import URL
from canari.maltego.entities import Website

from common import msmodule


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
    label='Website to URL [Mnemosyne]',
    description='Returns URLs extracted with automated tools from The Honeynet Project.',
    uuids=['mnemtego.v1.WebsiteToURLs'],
    inputs=[('Mnemtego', Website)],
    debug=True
)
def dotransform(request, response):
    url = request.value
    regex = '.*{0}(/|:)'.format(re.escape(url))
    json_dict = msmodule.query('/urls?url_regex={0}'.format(regex))

    if len(json_dict['urls']) > 0:
        for url in json_dict['urls']:
            entity = URL('woopsa')
            entity.fqdn = url['url']
            response += entity
    return response
