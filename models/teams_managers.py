from db import db


class TeamsManagers(db.Model):
    __tablename__ = "teams_managers"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    manager_id = db.Column(db.Integer, db.ForeignKey("users.id"))
