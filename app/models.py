from app.extensions import db
from werkzeug.security import generate_password_hash
from sqlalchemy import event


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', back_populates='products')
    images = db.Column(db.PickleType, nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "description": self.description,
            "category": self.category.as_dict() if self.category else None,
            "images": self.images
        }


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(200))
    products = db.relationship('Product', back_populates='category')

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    avatar = db.Column(db.String(200))

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "email": self.email,
            "avatar": self.avatar
        }


@event.listens_for(User, 'before_insert')
def hash_user_password_before_insert(mapper, connect, target):
    if target.password:
        target.password = generate_password_hash(target.password)


@event.listens_for(User, 'before_update')
def hash_user_password_before_update(mapper, connect, target):
    if target.password:
        target.password = generate_password_hash(target.password)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    originalname = db.Column(db.String(200), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "originalname": self.originalname,
            "filename": self.filename,
            "location": self.location
        }