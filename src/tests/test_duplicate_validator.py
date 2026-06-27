
from src.tests.factories import make_product
from src.validators.duplicate_validator import DuplicateValidator

def test_long_meta_titles ():

    product1 = make_product(
        meta_title = "A"*60,
        image_url= "test1.png",
        name= "Test Product",
        slug= "test-product",
        url= "/test-product",
        hero_title= "Test Hero Title",
        hero_text= "Test Hero Text",
        meta_description= "B" * 150,
        image_alt= "Test Image",
    )

    product2 = make_product(
        meta_title = "A"*60,
        image_url= "test1.png",
        name= "Test1 Product",
        slug= "test-product1",
        url= "/test-product1",
        hero_title= "Test1 Hero Title",
        hero_text= "Test1 Hero Text",
        meta_description= "A" * 150,
        image_alt= "Test1 Image",
    )
    
    validator = DuplicateValidator() 
    results = validator.validate([product1, product2]) 

    assert len(results) == 1
    assert results[0].field == "meta_title"
    assert results[0].severity == "ERROR"

    # product = Product (
        #     name="Dragon Fruit Powder", 
        #     hero_title="Premium Dragon Fruit",
        #     meta_title = "A"*70, 
        #     meta_description = "B"*170, 
        #     image_url = "test.png",
        #     image_alt= "Premium Quality Dragon Fruit Powder"
    # )

