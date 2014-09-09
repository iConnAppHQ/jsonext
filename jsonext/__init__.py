"""JSON-rendering helpers.

This module provides mixins for the stdlib :class:`json.JSONEncoder` class,
adding serialization methods for other object types, such as
:class:`~datetime.datetime` objects or iterables.

All these are ready to use by using :data:`~jsonext.dumps`.
"""

from functools import partial
import simplejson as json

from .mixins import JSONDateTimeMixin, JSONIterableMixin, JSONAsDictMixin, \
    JSONStringifyMixin, JSONPhoneNumberMixin, JSONChoiceMixin


class JSONEncoder(JSONDateTimeMixin, JSONIterableMixin, JSONAsDictMixin,
                  JSONPhoneNumberMixin, JSONChoiceMixin, JSONStringifyMixin,
                  json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        kwargs['ensure_ascii'] = False
        super(JSONEncoder, self).__init__(*args, **kwargs)


dumps = partial(json.dumps, cls=JSONEncoder)
