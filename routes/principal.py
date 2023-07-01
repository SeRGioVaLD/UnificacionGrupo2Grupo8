from flask import Blueprint, render_template as rt
from utils.clean_cache import borrar_cache

bp = Blueprint('principal', __name__, url_prefix="/principal") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/<tipo>/<id>')
def principal(id,tipo):
    borrar_cache(["Vacio.png"])
    return rt("principal.html",tipo = tipo, id = id)