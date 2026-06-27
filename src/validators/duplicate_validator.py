from dataclasses import field
from src.validators.base_validator import BaseValidator
from src.validators.validation_result import ValidationResult


class DuplicateValidator(BaseValidator):
    def validate(self, products):

        results = []

        results.extend(
            self.check_duplicate(
                products,
                field = "url",
            )

        )

        results.extend(
            self.check_duplicate(
                products,
                field = "meta_title",
            )

        )

        results.extend(
            self.check_duplicate(
                products,
                field = "meta_description",
            )

        )

        results.extend(
            self.check_duplicate(
                products,
                field = "name"
            )

        )

        return results

    def check_duplicate(self, products, field):

        results = []

        seen = {}

        for product in products: 

            value = getattr(product, field)

            if not value:
                continue

            if value in seen: 
                results.append(
                    ValidationResult(
                        product = product.name, 
                        field = field, 
                        severity="ERROR",
                        message = f"Duplicate {field} Detected!",
                        recommendation=f"Ensure Unique {field} Value",
                    )
                )

            else:

                seen[value] = product.name
        return results

