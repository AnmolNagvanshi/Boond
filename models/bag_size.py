from db import db


class BagSize(db.Model):
    __tablename__ = "bag_sizes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    volume = db.Column(db.Integer, nullable=False)

    bag = db.relationship('BloodBag', backref='bag_size', lazy='dynamic')

    def __repr__(self):
        return f"{self.volume} ml"

