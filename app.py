from flask import Flask
from utils.config import Config
from flask import Flask
from utils.config import Config

def crear_app():
    app = Flask(__name__)
    #CARGAR CONFIGURACION
    app.config.from_object(Config)
    #BLUEPRINTS
    from routes import login
    app.register_blueprint(login.bp)
    
    from routes import principal
    app.register_blueprint(principal.bp)
    
    from routes import vista
    app.register_blueprint(vista.bp)
    
    from routes import cotizaciones  # Importa el blueprint 'cotizaciones'
    app.register_blueprint(cotizaciones.bp)  # Registra el blueprint 'cotizaciones'
    
    from routes import solicitud_cotizacion
    app.register_blueprint(solicitud_cotizacion.bp)
    
    from routes import boleta
    app.register_blueprint(boleta.bp)
    
    from routes import contratos
    app.register_blueprint(contratos.routes)
    return app