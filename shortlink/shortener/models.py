"""
This module does contain models in the strictest sense, as URL does
not inherent the Django class Model. Since no DB is required for this
assignment, I chose a regular class to represent the URL object. It is the
only "model" in this module.
"""
from datetime import datetime


class URL:
    """
    This class represents an encoded url.

    Static variables:
    :id: id keeps track of the number of urls in the server and provide means
    for encoding them, as it is unique

    Instance variables:
    :long_version: unencoded original url
    :short_version: encoded version of original url
    :created_at: time at which the url was encoded
    """
    id = 0

    def __init__(self, long_version, short_version, created_at=datetime.now()):
        """
        URL constructor
        """
        self.long_version = long_version
        self.short_version = short_version
        self.created_at = created_at or datetime.now()
        URL.id += 1

    def __str__(self):
        """
        Provides string representation of a url object
        """
        return f'''
            Original url: {self.long_version}
            Shortened version: {self.short_version}
        '''
