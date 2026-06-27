from src.validators import validation_result


class ValidationEngine:

    def __init__(self, validators):
        self.validators = validators

    def run(self, products):
        results = []

        for validator in self.validators: 
            print(
                f"Running Validator {validator.__class__.__name__}....."
            )

            results.extend(
                validator.validate(products)
            )
        return results


