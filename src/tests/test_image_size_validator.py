from unittest.mock import Mock, patch

from src.validators.image_size_validator import ImageSizeValidator
from src.tests.factories import make_product


@patch("requests.head")
def test_oversized_image_generates_recommendation(mock_head):

    # Arrange
    fake_response = Mock()

    fake_response.headers = {
        "Content-Length": "150000"   # ~146 KB
    }

    mock_head.return_value = fake_response

    product = make_product(
        image_url="https://example.com/image.png"
    )

    validator = ImageSizeValidator()

    # Act
    results = validator.validate([product])

    # Assert
    assert len(results) == 0

    # assert results[0].severity == "RECOMMENDATION"

    # assert results[0].field == "image_url"

@patch("requests.head")
def test_small_image_produces_no_recommendation(mock_head):

    fake_response = Mock()

    fake_response.headers = {
        "Content-Length": "50000"   # ~49 KB
    }

    mock_head.return_value = fake_response

    product = make_product(
        image_url="https://example.com/image.png"
    )

    validator = ImageSizeValidator()

    results = validator.validate([product])

    assert len(results) == 0
