from Watch_it import db


class User(db.Model):
    """
    This class is for ORM (User table)
    """

    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(15))
    browser = db.Column(db.String(15))
    ip = db.Column(db.String(15))
    country = db.Column(db.String(40))

    def __init__(self, platform, browser, ip, country):
        """__init__"""

        self.platform = platform
        self.browser = browser
        self.ip = ip
        self.country = country

    def __repr__(self):
        return '<User %s>' % self.ip


db.create_all()
