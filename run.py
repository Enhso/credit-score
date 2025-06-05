from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run() # Le mode debug est contrôlé par FLASK_DEBUG=1 dans .env
