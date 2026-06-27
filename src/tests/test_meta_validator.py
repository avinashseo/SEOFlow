
from src.tests.factories import make_product
from src.validators.meta_validator import MetaValidator

def test_long_meta_titles ():

    product = make_product(
        meta_title = "A"*70
    )
    # product = Product (
        #     name="Dragon Fruit Powder", 
        #     hero_title="Premium Dragon Fruit",
        #     meta_title = "A"*70, 
        #     meta_description = "B"*170, 
        #     image_url = "test.png",
        #     image_alt= "Premium Quality Dragon Fruit Powder"
    # )

    validator = MetaValidator() 
    results = validator.validate([product]) 

    assert len(results) == 1
    assert results[0].field == "meta_title"
    assert results[0].severity == "WARNING"

