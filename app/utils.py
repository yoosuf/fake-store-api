def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# Attach the as_dict method to all models
from app.models import Product, Category, User, File

for cls in [Product, Category, User, File]:
    cls.as_dict = as_dict
