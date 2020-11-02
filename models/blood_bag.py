from datetime import datetime
from db import db
from utilities.blood_group import BloodGroupType


class BloodBag(db.Model):
    __tablename__ = "blood_bags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blood_bank_id = db.Column(db.Integer, db.ForeignKey('blood_banks.id'), nullable=False)
    bag_size_id = db.Column(db.Integer, db.ForeignKey('bag_sizes.id'), nullable=False)

    blood_group = db.Column(db.Enum(BloodGroupType), nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)
    collection_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)

    # blood_bank = db.relationship('BloodBag', backref=db.backref('blood_bags', lazy='dynamic'))
    # bag_size = db.relationship("BagSize", foreign_keys=[bag_size_id], lazy='dynamic')

    def total_ml(self) -> int:
        return self.bag_size.volume * self.quantity

    def __repr__(self):
        return f"{self.blood_bank_id} has {self.quantity} bags of \
        ({self.bag_size}) of {self.blood_group.name} group"

