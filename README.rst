Mnemtego
========

This project will provide `Maltego <http://www.paterva.com/web6/products/maltego.php>`_
transforms for `Mnemosyne <https://github.com/johnnykv/mnemosyne>`_.

Install
=======
This project is not ready for production yet, but if you REALLY want to try it out - follow this procedure::

  pip install canari
  git clone https://github.com/johnnykv/mnemtego
  cd mnemtego
  python setup.py install
  canari install-package mnemtego

Transforms
==========

Currently the following transforms are available:

* IP to honeypot attacks.
* IP to attacked protocols.
* Domain to URL's.
 
  * Expands a domain to all URL's within that domain which somehow has been reported on HPFeeds.

* URL to (potential) malware extractions (hashes).

  * Expands a URL to hashes of all reported extractions (PDF, Javascript, SWF, JAR, etc).
  * The binary itself will have to be downloaded manually from mnemosyne.

* Extractions (hashes) to URL's.

  * Expands a hash to all URL which has been serving this file.

Example graph
=============

The following graph shows how a query on a specific .ru domain revealed that it was serving a piece of Adobe Flash (SWF) malware.
Furthermore it was revealed that this `specific malware (a5a1308ee3ca7f75fe85fe4d9a14752f)
<https://www.virustotal.com/en/file/3beb8ae0ce0ba1c7a8235d93aefcadded2ab7917414b70ce424836ad0ca4a721/analysis/>`_ 
was also served from 8 other sites.


.. image:: http://img203.imageshack.us/img203/3440/maltegoexample.png
