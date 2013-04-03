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
    description='Returns hashes of malicious files (javascript, binaries, etc) extracted from the specified url',
    uuids=['mnemtego.v1.URLToExtraction'],
    inputs=[('Mnemtego', URL)],
    debug=True
)
def dotransform(request, response):

    url = request.value

    regex = '^{0}'.format(re.escape(url))
    json_dict = msmodule.query('urls?url_regex={0}'.format(regex))

    if len(json_dict['urls']) > 0:
        if 'extractions' in json_dict['urls'][0]:
            extractions = json_dict['urls'][0]['extractions']

            valid_hash_fields = set(['md5', 'sha1', 'sha512'])

            for e in extractions:
                has_hash_keys = valid_hash_fields.intersection(set(e['hashes'].keys()))

                #entity = MnemosyneExtraction('{0} [{1}]'.format(e['hashes']['sha1'], 'SHA1'))
                entity = MnemosyneExtraction('Unknown')

                for k in has_hash_keys:
                    setattr(entity, k, e['hashes'][k])

                query = msmodule.query('files?hash={0}&no_data'.format(entity.md5))['files']

                if len(query) > 0 and 'content_guess' in query[0]:
                    entity.content_guess = query[0]['content_guess']
                else:
                    entity.content_guess = 'Unknown'

                entity.value = entity.content_guess

                response += entity

    return response
