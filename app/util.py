"""
Various Classes used by the app.
"""
from math import ceil
from app.dbi import fetch_from_table


# class User(UserMixin):
#     """
#     Class for handling users
#
#     Attributes
#     - is_authenticated: Returns True if the user is authenticated
#     - is_active: Returns True if this is an active
#     - is_anonymous: Returns True if this is an anonymous user.
#     """
#     def __init__(self):
#         """Inititialize object """
#         self.is_authenticated = False
#         self.is_active = False
#         self.is_anonymous = False
#
#     def get_id(self):
#         """
#         Returns a unicode that uniquely identifies this user, and can be used
#         to load the user from the user_loader callback. Note that this must be
#         a unicode - if the ID is natively an int or some other type, you will
#         need to convert it to unicode.
#         """
#         return self.id

class Pagination(object):
    """from Armin Ronacher
    Handles pagination
        """

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num
