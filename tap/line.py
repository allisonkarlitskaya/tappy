# Copyright (c) 2014, Matt Layman


class Line(object):
    """Base type for TAP data.

    TAP is a line based protocol. Thus, the most primitive type is a line.
    """
    @property
    def category(self):
        raise NotImplementedError


class Result(Line):
    """Information about an individual test line."""

    def __init__(self, ok, number=None, description='', directive=None):
        self._ok = ok
        if number:
            self._number = int(number)
        else:
            # The number may be an empty string so explicitly set to None.
            self._number = None
        self._description = description
        self.directive = directive

    @property
    def category(self):
        return 'test'

    @property
    def ok(self):
        return self._ok

    @property
    def number(self):
        return self._number

    @property
    def description(self):
        return self._description

    @property
    def skip(self):
        return self.directive.skip

    @property
    def todo(self):
        return self.directive.todo


class Diagnostic(Line):
    """A diagnostic line (i.e. anything starting with a hash)."""

    def __init__(self, text):
        self._text = text

    @property
    def category(self):
        return 'diagnostic'

    @property
    def text(self):
        return self._text


class Bail(Line):
    """A bail out line (i.e. anything starting with 'Bail out!')."""

    def __init__(self, reason):
        self._reason = reason

    @property
    def category(self):
        return 'bail'

    @property
    def reason(self):
        return self._reason


class Unknown(Line):
    """A line that represents something that is not a known TAP line.

    This exists for the purpose of a Null Object pattern.
    """
    @property
    def category(self):
        return 'unknown'

# TODO: Plan line
# TODO: Version line