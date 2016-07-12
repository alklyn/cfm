

class User(UserMixin):
    """
    Class for handling users

    Attributes
    - is_authenticated: Returns True if the user is authenticated
    - is_active: Returns True if this is an active
    - is_anonymous: Returns True if this is an anonymous user.
    """
    def __init__(self):
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = False

    def get_id(self):
        """
        Returns a unicode that uniquely identifies this user, and can be used
        to load the user from the user_loader callback. Note that this must be
        a unicode - if the ID is natively an int or some other type, you will
        need to convert it to unicode.
        """
        pass
