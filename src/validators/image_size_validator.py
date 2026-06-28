import requests

from src.validators.base_validator import BaseValidator
from src.validators.validation_result import ValidationResult

class ImageSizeValidator(BaseValidator): 
    
    MAX_IMAGE_SIZE_KB = 100 

    def validate(self, products):
        
        results = []

        for product in products: 
            if not product.image_url: 
                continue

            result = self.check_image_size(product)

            if result: 
                results.append(result)

        return results

    def check_image_size(self, product):

        try: 
            response = requests.head(
                product.image_url, 
                timeout=10, 
                allow_redirects=True
            )

            content_length = response.headers.get(
                "content-length"
            )

            if not content_length: 
                return None

            size_kb = int(content_length)/1024

            if size_kb > self.MAX_IMAGE_SIZE_KB:
                return ValidationResult(
                    product = product.name, 
                    field = "image_url",
                    severity = "RECOMMENDATION",
                    message = (
                        f"Image size is "
                        f"{size_kb:.1f} KB. "
                        f"Compress below "
                        f"{self.MAX_IMAGE_SIZE_KB} KB "
                        f"for better page load speed."
                    ),
                )

        except Exception as error: 
            print(
                f"⚠️ Could not check "
                f"{product.image_url}"
            )

            print(error)
        return None


