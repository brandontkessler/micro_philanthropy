from app import create_app, db
from app.models import User

class BaseTest:
    def set_up(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        return

    def tear_down(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        return

    def load_user(self, email, password):
        user = User(email=email)
        user.hash_password(pw=password)
        return user
