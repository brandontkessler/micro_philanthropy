import os
from app import create_app, db
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'development')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

@app.cli.command('setup_db')
def setup_app():
    db.create_all()
