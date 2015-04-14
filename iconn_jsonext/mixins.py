import datetime
import times
from bson import objectid

class JSONDateTimeMixin(object):
    """A mixin for JSONEncoders, encoding :class:`datetime.datetime` and
    :class:`datetime.date` objects by converting them to strings that can be
    parsed by all modern browsers JS Date() object.

    All timestamps are converted to UTC before being serialized.

    Date objects simply use :meth:`~datetime.date.isoformat`.

    >>> import jsonext
    >>> from datetime import datetime
    >>> dt = datetime(2013, 11, 17, 12, 00, 00)  # Python 3.3.3 release!
    >>> jsonext.dumps(dt)
    '"2013-11-17T12:00:00+00:00"'
    >>> d = dt.date()
    >>> d
    datetime.date(2013, 11, 17)
    >>> jsonext.dumps(d)
    '"2013-11-17"'
    """
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return times.format(o, 'Zulu')
        if isinstance(o, datetime.date):
            return o.isoformat()
        return super(JSONDateTimeMixin, self).default(o)


class JSONIterableMixin(object):
    """A mixin for JSONEncoders, encoding any iterable type by converting it to
    a list.

    Especially useful for SQLAlchemy results that look a lot like regular lists
    or iterators, but will trip up the encoder. Beware of infinite
    generators.

    >>> import jsonext
    >>> gen = (i**2 for i in range(10))
    >>> jsonext.dumps(gen)
    '[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'
    """
    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        return super(JSONIterableMixin, self).default(o)


class JSONStringifyMixin(object):
    """A mixing for JSONEncoders, encoding any object that has a ``__str__``
    method with the return value of said function.

    >>> import jsonext
    >>> from decimal import Decimal as D
    >>> x = D('123.456')
    >>> jsonext.dumps(x)
    '"123.456"'
    >>> from datetime import timedelta
    >>> t = timedelta(days=5, seconds=12345)
    >>> jsonext.dumps(t)
    '"5 days, 3:25:45"'
    """
    def default(self, o):
        if hasattr(o, '__str__'):
            return str(o)
        return super(JSONStringifyMixin, self).default(o)


class JSONMongoBsonMixin(object):
    """A mixing for JSONEncoders, encoding Mongo objectids.
    """
    def default(self, o):
        if isinstance(o, objectid.ObjectId):
            return str(o)
        return super(JSONMongoBsonMixin, self).default(o)

