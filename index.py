from app import crear_app
from utils.db import db

app = crear_app()

#   SE VINCULA EL DB CON NUESTRA APP
db.init_app(app)

#   METODO MAIN
if __name__ == '__main__':
    app.run(debug=True)