"""JSON-rendering helpers.

This module provides mixins for the stdlib :class:`json.JSONEncoder` class,
adding serialization methods for other object types, such as
:class:`~datetime.datetime` objects or iterables.

All these are ready to use by using :data:`~jsonext.dumps`.
"""

import simplejson as json

try:
    from flask import current_app
except:
    pass

from .mixins import JSONDateTimeMixin, JSONIterableMixin, JSONAsDictMixin, \
    JSONStringifyMixin, JSONPhoneNumberMixin, JSONChoiceMixin


class JSONEncoder(JSONDateTimeMixin, JSONIterableMixin, JSONAsDictMixin,
                  JSONPhoneNumberMixin, JSONChoiceMixin, JSONStringifyMixin,
                  json.JSONEncoder):
    pass


def dumps(*args, **kwargs):
    kwargs = {'cls': JSONEncoder}
    if globals().get('current_app') is not None and 'ensure_ascii' not in kwargs:
        kwargs['ensure_ascii'] = current_app.config['DEBUG']
    return json.dumps(*args, **kwargs)
