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
    label='URL to extractions [Mnemosyne]',
    description='Returns checksums of malicious files (javascript, binaries, etc) extracted from the url',
    uuids=['mnemosyne.v1.MnemosyneURLToExtractions'],
    inputs=[('Mnemosyne', URL)],
    debug=True
)
def dotransform(request, response):

    url = request.value

    regex = '^{0}'.format(re.escape(url))
    json_dict = msmodule.query('/urls?url_regex={0}'.format(regex))

    if len(json_dict['urls']) > 0:
        if 'extractions' in json_dict['urls'][0]:
            extractions = json_dict['urls'][0]['extractions']

            valid_hash_fields = set(['md5', 'sha1', 'sha512'])

            for e in extractions:
                has_hash_keys = valid_hash_fields.intersection(set(e['hashes'].keys()))

                entity = MnemosyneExtraction('{0} [{1}]'.format(e['hashes']['md5'], 'MD5'))
                for k in has_hash_keys:
                    entity.k = e['hashes'][k]

                #TODO: mnemo API must add this
                #entity.hpfeed_id = e['hpfeed_id']
                response += entity

    return response
