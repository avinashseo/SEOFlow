from dataclasses import dataclass


@dataclass(slots=True)
class ValidationResult:
    product: str
    field: str
    severity: str
    message: str
    recommendation: str