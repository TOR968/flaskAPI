from db import db


class ClubModel(db.Model):
    __tablename__ = "clubs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    main_stadium = db.Column(db.String(50), nullable=False)
    est = db.Column(db.Date, nullable=False)
    teams = db.relationship("TeamModel", back_populates="club", lazy="dynamic")