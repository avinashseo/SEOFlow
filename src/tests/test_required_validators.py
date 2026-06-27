from src.models.product import Product
from src.tests.factories import make_product
from src.validators.required_validator import RequiredValidator


def test_missing_image_url():

    product = make_product(
        image_url = ""
    )

    # product = Product(
    #     name="Dragon Fruit Powder", 
    #     hero_title = "Premium Dragon Fruit Powder", 
    #     meta_title = "Buy Dragon Fruit Powder",
    #     meta_description = "Buy premium quality dragon fruit powder from India. Contact Frukty today.",
    #     image_url = "", 
    #     image_alt= "Premium Quality Dragon Fruit Powder" 
    

    validators = RequiredValidator()
    results = validators.validate([product])

    assert len(results) ==1

    assert results[0].field == "image_url" 

    assert results[0].severity =="ERROR"


