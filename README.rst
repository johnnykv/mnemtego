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
