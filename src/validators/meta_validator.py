from numpy.ma import product
from src.validators.base_validator import BaseValidator
from src.validators.validation_result import ValidationResult


class MetaValidator(BaseValidator): 
    
    def validate_length(
        self, 
        product,
        field,
        value, 
        max_length, 
        min_length, 
    ):
        result = []

        length = len(value)

        if length < min_length:

            result.append(
                ValidationResult(
                    product = product.name, 
                    field = field, 
                    severity="WARNING",
                    message=f"{field} is too small! ({length} chars.)" ,
                    recommendation="Increase the Meta title length upto 60 chars", 
                )
                
            )

        elif length > max_length:

            result.append(
                ValidationResult(
                    product = product.name, 
                    field = field, 
                    severity="WARNING",
                    message=f"{field} is too Long! ({length} chars.) ",
                    recommendation="Keep the Meta title length upto 60 chars", 

                )
            )

        return result
    def validate(self, products):
        
        results = []

        for product in products:

            results.extend(
                self.validate_length(
                    product, 
                    field = 'meta_title',
                    value = product.meta_title,
                    min_length=30,
                    max_length=60,
                )
            )

            results.extend(
                self.validate_length(
                    product, 
                    field="meta_description", 
                    value = product.meta_description, 
                    min_length = 120, 
                    max_length=160,
                )
            )

        return results