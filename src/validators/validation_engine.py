from src.validators.validation_result import ValidationResult
from src.validators.image_size_validator import (ImageSizeValidator, )


class ValidationEngine:

    def __init__(self, validators):
        self.validators = validators

    def run(self, products):
        results = []

        for validator in self.validators: 
            print(
                f"🔍 Running Validator {validator.__class__.__name__}....."
            )

            results.extend(
                validator.validate(products)
            )
        return results


