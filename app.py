"""
SEOFlow Entry Point
"""

from src.config.profile_loader import ProfileLoader
from src.readers.csv_reader import CSVReader
from src.mappers.product_mapper import ProductMapper


def main():

    print("=" * 50)
    print("SEOFlow")
    print("Programmatic SEO Automation Toolkit")
    print("=" * 50)

    # Load profile
    profile = ProfileLoader.load("mpg")

    print("\n✅ Profile loaded successfully")

    # Read CSV
    reader = CSVReader("data/input/products.csv")

    dataframe = reader.read()

    print(f"✅ CSV loaded successfully")
    print(f"Rows found: {len(dataframe)}")

    # Map products
    mapper = ProductMapper(profile)

    products = mapper.map(dataframe)

    print(f"✅ Products mapped successfully")
    print(f"Products created: {len(products)}")

    print("\nSample Product")
    print("-" * 50)

    product = products[0]

    print(f"Name           : {product.name}")
    print(f"Hero Title     : {product.hero_title}")
    print(f"Meta Title     : {product.meta_title}")
    print(f"Image URL      : {product.image_url}")
    print(f"Image ALT      : {product.image_alt}")


if __name__ == "__main__":
    main()