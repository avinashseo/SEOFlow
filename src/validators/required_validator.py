from src.validators.base_validator import BaseValidator
from src.validators.validation_result import ValidationResult


class RequiredValidator(BaseValidator):

    REQUIRED_FIELDS = [
        "name",
        "hero_title",
        "meta_title",
        "meta_description",
        "image_url",
    ]

    def validate(self, products):

        results = []

        for product in products:

            for field in self.REQUIRED_FIELDS:

                value = getattr(product, field)

                if not value:

                    results.append(
                        ValidationResult(
                            product=product.name or "Unknown Product",
                            field=field,
                            severity="ERROR",
                            message="Required field is missing",
                            recommendation=f"Provide a value for '{field}'",
                        )
                    )

        return results