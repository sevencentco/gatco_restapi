"""
    gatco_restapi
    ~~~~~~~~~~~~~~~~~~

    Gatco-RestAPI is a `Gatco <https://github.com/gonrin/gatco>`_ extension which
    facilitates the creation of ReSTful JSON APIs. It is compatible with models
    which have been described using `SQLAlchemy <http://sqlalchemy.org>`_.

    :copyright:2011 by Lincoln de Sousa <lincoln@comum.org>
    :copyright: 2012, 2013, 2014, 2015 Jeffrey Finkelstein
                <jeffrey.finkelstein@gmail.com> and contributors.
    :copyright:2016, 2017 by Cuong Nguyen Cao <cuongnc.coder@gmail.com>
    :license: MIT

"""

#: The current version of this extension.
#:
#: This should be the same as the version specified in the :file:`setup.py`
#: file.
__version__ = '0.17.0'

# make the following names available as part of the public API
from .helpers import url_for
from .manager import APIManager
from .manager import IllegalArgumentError
from .views import ProcessingException
