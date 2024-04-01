from db import db  # Importing our database


class TeamModel(db.Model):  # Inheriting our model from db.Model
    __tablename__ = "teams"  # Specifying the table name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    league = db.Column(db.String(50), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"), nullable=False)
    club = db.relationship("ClubModel", back_populates="teams")
    managers = db.relationship(
        "UserModel", back_populates="teams", secondary="teams_managers"
    )
    players = db.relationship("PlayerModel", back_populates="team", lazy="dynamic")
