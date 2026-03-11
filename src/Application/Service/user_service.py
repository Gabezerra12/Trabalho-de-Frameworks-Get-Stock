from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db 

class UserService:
    @staticmethod
    def create_user(name, cnpj, email, celular, password):
        user = User(name=name, cnpj=cnpj, email=email, celular=celular, password=password, status='inactive')
        db.session.add(user)
        db.session.commit()
        return UserDomain(user.id, user.name, user.cnpj, user.email, user.celular, user.password, user.status)

    @staticmethod
    def _generate_activation_code():
        from random import randint
        return f"{randint(1000, 9999)}"
