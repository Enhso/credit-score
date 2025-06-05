import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv()

# Initialisation des extensions (sans application pour l'instant)
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class_name=None):
    """
    Factory pattern pour créer l'application Flask.
    """
    app = Flask(__name__)

    # Configuration de l'application
    # Utilise la classe de configuration passée en argument ou charge depuis les variables d'environnement
    if config_class_name:
        app.config.from_object(config_class_name)
    else:
        # Configuration par défaut à partir des variables d'environnement
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Recommandé de le mettre à False
        app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
        # Ajoute d'autres configurations JWT si nécessaire, ex:
        # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    # Initialisation des extensions avec l'application
    db.init_app(app)
    migrate.init_app(app, db) # Flask-Migrate a besoin de l'app et de db
    jwt.init_app(app)

    # Importer et enregistrer les Blueprints (routes)
    # (Nous le ferons plus tard quand les routes seront définies)
    # from .routes import main_bp # Exemple
    # app.register_blueprint(main_bp)

    # Importer les modèles pour que Flask-Migrate puisse les détecter
    # (Assure-toi que models.py existe, même vide pour l'instant)
    from . import models

    @app.route('/hello')
    def hello():
        return "Bonjour, la configuration initiale fonctionne !"

    return app
