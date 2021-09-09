from datetime import datetime


# TODO: document this class
class URL:
    id = 0

    def __init__(self, long_version, short_version, created_at=datetime.now()):
        self.long_version = long_version
        self.short_version = short_version
        self.created_at = created_at or datetime.now()
        URL.id += 1

    def __str__(self):
        return f'''
            Original url: {self.long_version}
            Shortened version: {self.short_version}
        '''
