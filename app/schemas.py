from marshmallow import Schema, fields, validate, ValidationError


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True)
    description = fields.Str()
    category = fields.Nested(CategorySchema, dump_only=True)
    category_id = fields.Int(load_only=True, required=True)
    images = fields.List(fields.Str(), required=True)

    def post_dump(self, data, many, **kwargs):
        return {
            "data": data,
            "message": "Success" if not self.context.get('error') else "Failed",
            "error": self.context.get('error') or None
        }

    def contextualize(self, data):
        return {
            "data": data,
            "message": "Success" if not self.context.get('error') else "Failed",
            "error": self.context.get('error') or None
        }


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    image = fields.Str(required=True)

    def post_dump(self, data, many, **kwargs):
        return {
            "data": data,
            "error": self.context.get('error') or None
        }

    def contextualize(self, data):
        return {
            "data": data,
            "error": self.context.get('error') or None
        }


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
