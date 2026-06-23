"""
Maps a pandas DataFrame into Product objects.
"""

from typing import List

from src.models.product import Product


class ProductMapper:

    def __init__(self, mapping: dict):

        self.mapping = mapping

    def map(self, dataframe) -> List[Product]:

        products = []

        for _, row in dataframe.iterrows():

            product = Product(

                name=row.get(self.mapping["name"], ""),

                slug=row.get(self.mapping["slug"], ""),

                url=row.get(self.mapping["url"], ""),

                hero_title=row.get(self.mapping["hero_title"], ""),

                hero_text=row.get(self.mapping["hero_text"], ""),

                meta_title=row.get(self.mapping["meta_title"], ""),

                meta_description=row.get(
                    self.mapping["meta_description"], ""
                ),

                og_title=row.get(self.mapping["og_title"], ""),

                og_description=row.get(
                    self.mapping["og_description"], ""
                ),

                image_url=row.get(self.mapping["image_url"], ""),

                image_alt=row.get(self.mapping["image_alt"], ""),

                applications=row.get(
                    self.mapping["applications"], ""
                ),

                benefits=row.get(self.mapping["benefits"], ""),

                pack_sizes=row.get(self.mapping["pack_sizes"], ""),

                moq=row.get(self.mapping["moq"], ""),

                lead_time=row.get(self.mapping["lead_time"], ""),

                shelf_life=row.get(
                    self.mapping["shelf_life"], ""
                )

            )

            products.append(product)

        return products