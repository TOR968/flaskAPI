from flask.views import MethodView
from flask_smorest import Blueprint
from models.club import ClubModel
from schemas import ClubSchema

blp = Blueprint("clubs", __name__, description="Operations on the clubs")


@blp.route("/clubs/<int:club_id>")
class Club(MethodView):
    @blp.response(200, ClubSchema)
    def get(self, club_id):
        return ClubModel.query.get_or_404(club_id)
