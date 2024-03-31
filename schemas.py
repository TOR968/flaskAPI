from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    full_name = fields.Str(required=True)


class PlainPlayerSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    position = fields.Str(required=True)
    number = fields.Int(required=True)


class PlainClubSchema(Schema):
    name = fields.Str(required=True)


class PlainTeamSchema(Schema):
    title = fields.Str(required=True, unique=True)
    club = fields.Nested(PlainClubSchema(), dump_only=True)


class UserSchema(PlainUserSchema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    teams = fields.List(fields.Nested(PlainTeamSchema()), dump_only=True)


class ClubSchema(PlainClubSchema):
    id = fields.Int(dump_only=True)
    country = fields.Str(required=True)
    city = fields.Str(required=True)
    main_stadium = fields.Str(required=True)
    est = fields.Date(required=True)
    teams = fields.List(fields.Nested(PlainTeamSchema()), dump_only=True)


class PlayerSchema(PlainPlayerSchema):
    id = fields.Int(dump_only=True)
    team_id = fields.Int(load_only=True)
    team = fields.Nested(PlainTeamSchema(), dump_only=True)


class TeamSchema(PlainTeamSchema):
    id = fields.Int(dump_only=True)
    league = fields.Str(required=True)
    club_id = fields.Int(required=True, load_only=True)
    managers = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)
    players = fields.List(fields.Nested(PlainPlayerSchema()), dump_only=True)


class TeamUpdateSchema(Schema):
    title = fields.Str()
    league = fields.Str()


class PlayerUpdateSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    position = fields.Str()
    number = fields.Int()
    team_id = fields.Int()