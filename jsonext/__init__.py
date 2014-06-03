"""JSON-rendering helpers.

This module provides mixins for the stdlib :class:`json.JSONEncoder` class,
adding serialization methods for other object types, such as
:class:`~datetime.datetime` objects or iterables.

All these are ready to use by using :data:`~jsonext.dumps`.
"""

import functools
import simplejson as json

from .mixins import JSONDateTimeMixin, JSONIterableMixin, JSONAsDictMixin, \
    JSONStringifyMixin, JSONPhoneNumberMixin, JSONChoiceMixin


class JSONEncoder(JSONDateTimeMixin, JSONIterableMixin, JSONAsDictMixin,
                  JSONPhoneNumberMixin, JSONChoiceMixin, JSONStringifyMixin,
                  json.JSONEncoder):
    pass


dumps = functools.partial(json.dumps, cls=JSONEncoder)
