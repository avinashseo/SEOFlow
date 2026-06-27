
from src.models.product import Product

def make_product(**overrides):
    defaults = {
        "name": "Test Product",
        "slug": "test-product",
        "url": "/test-product",
        "hero_title": "Test Hero Title",
        "hero_text": "Test Hero Text",
        "meta_title": "Test Meta Title",
        "meta_description": "A" * 150,
        "image_url": "test.png",
        "image_alt": "Test Image",}

    

    defaults.update(overrides)

    return Product(**defaults)