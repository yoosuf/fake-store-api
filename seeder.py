import random
from faker import Faker
from app import create_app, db
from app.models import User, Product, Category

app = create_app()
app.app_context().push()
faker = Faker()


def seed_users(num_users=10):
    for _ in range(num_users):
        user = User(
            name=faker.name(),
            role=random.choice(['admin', 'user']),
            email=faker.email(),
            password=faker.password(),
            avatar=faker.image_url()
        )
        db.session.add(user)
    db.session.commit()


def seed_categories(num_categories=5):
    for _ in range(num_categories):
        category = Category(
            name=faker.word(),
            image=faker.image_url()
        )
        db.session.add(category)
    db.session.commit()


def seed_products(num_products=20):
    category_ids = [category.id for category in Category.query.all()]
    for _ in range(num_products):
        product = Product(
            title=faker.word(),
            price=random.uniform(10.0, 100.0),
            description=faker.text(),
            category_id=random.choice(category_ids),
            images=[faker.image_url() for _ in range(random.randint(1, 3))]
        )
        db.session.add(product)
    db.session.commit()


def run_seeder():
    db.drop_all()
    db.create_all()

    seed_users()
    seed_categories()
    seed_products()


if __name__ == "__main__":
    run_seeder()
