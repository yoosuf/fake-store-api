import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import User as UserModel, Product as ProductModel, Category as CategoryModel, File as FileModel
from app.extensions import db

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)

class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        interfaces = (graphene.relay.Node,)

class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (graphene.relay.Node,)

class File(SQLAlchemyObjectType):
    class Meta:
        model = FileModel
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = SQLAlchemyConnectionField(User.connection)
    all_products = SQLAlchemyConnectionField(Product.connection)
    all_categories = SQLAlchemyConnectionField(Category.connection)
    all_files = SQLAlchemyConnectionField(File.connection)

    user = graphene.Field(User, id=graphene.Int())
    product = graphene.Field(Product, id=graphene.Int())
    category = graphene.Field(Category, id=graphene.Int())
    file = graphene.Field(File, id=graphene.Int())

    def resolve_user(self, info, id):
        return UserModel.query.get(id)

    def resolve_product(self, info, id):
        return ProductModel.query.get(id)

    def resolve_category(self, info, id):
        return CategoryModel.query.get(id)

    def resolve_file(self, info, id):
        return FileModel.query.get(id)

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        role = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        avatar = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, name, role, email, password, avatar):
        user = UserModel(name=name, role=role, email=email, password=password, avatar=avatar)
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)

class CreateProduct(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        price = graphene.Float(required=True)
        description = graphene.String()
        category_id = graphene.Int(required=True)
        images = graphene.List(graphene.String)

    product = graphene.Field(lambda: Product)

    def mutate(self, info, title, price, description, category_id, images):
        product = ProductModel(title=title, price=price, description=description, category_id=category_id, images=images)
        db.session.add(product)
        db.session.commit()
        return CreateProduct(product=product)

class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        image = graphene.String(required=True)

    category = graphene.Field(lambda: Category)

    def mutate(self, info, name, image):
        category = CategoryModel(name=name, image=image)
        db.session.add(category)
        db.session.commit()
        return CreateCategory(category=category)

class CreateFile(graphene.Mutation):
    class Arguments:
        originalname = graphene.String(required=True)
        filename = graphene.String(required=True)
        location = graphene.String(required=True)

    file = graphene.Field(lambda: File)

    def mutate(self, info, originalname, filename, location):
        file = FileModel(originalname=originalname, filename=filename, location=location)
        db.session.add(file)
        db.session.commit()
        return CreateFile(file=file)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_product = CreateProduct.Field()
    create_category = CreateCategory.Field()
    create_file = CreateFile.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)