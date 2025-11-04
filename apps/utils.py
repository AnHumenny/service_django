import re
from string import punctuation
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


def validate_email(value: str):
    """Validate the required field 'email' for admin-panel."""

    if not re.match(r'^[\w.-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', value):
        raise ValidationError("Invalid email format. Example: example@example.com")
    return value


def latinic_validation(string: str) -> bool:
    """Checking validate only Latin letters."""
    for i in [j for j in string if j.isalpha()]:
        if not i.isascii():
            return False
    return True


def check_password_regex(password: str):
    """
    Check password for complexity using regex."""
    if len(password) < 8:
        return False, "Make sure your password is at least 8 letters"

    checks = [
        (r'\d', "Make sure your password has a number in it"),
        (r'[A-Z]', "Make sure your password has a capital letter in it"),
        (r'[a-z]', "Make sure your password has a lowercase letter in it"),
        (rf'[{re.escape(punctuation)}]', "Make sure your password has a special character in it")
    ]

    for pattern, message in checks:
        if not re.search(pattern, password):
            return False, message

    if not latinic_validation(password):
        return False, "Make sure your password consists of Latin alphabet only"

    return True, None


def validate_phone_number(value):
    """Validate phone number format."""
    pattern = r'^\+?1?\d{9,15}$'
    if not re.match(pattern, value):
        raise ValidationError(
            _('%(value)s is not a valid phone number'),
            params={'value': value},
        )


@deconstructible
class IntegerFieldValidator:
    """A wrapper for Django's MinValueValidator and MaxValueValidator that allows None values."""

    def __init__(self, min_value=None, max_value=None):
        """Initialize the validator with optional minimum and/or maximum values."""
        self.min_value = min_value
        self.max_value = max_value

        self.min_validator = MinValueValidator(min_value) if min_value is not None else None
        self.max_validator = MaxValueValidator(max_value) if max_value is not None else None

    def __call__(self, value):
        """Validate the given value if it's not None."""
        if value is None:
            return
        if not isinstance(value, int):
            raise ValidationError("The value must be an integer.")
        if self.min_validator:
            self.min_validator(value)
        if self.max_validator:
            self.max_validator(value)

    def __eq__(self, other):
        """Compare this validator to another."""
        return (
                isinstance(other, IntegerFieldValidator)
                and self.min_value == other.min_value
                and self.max_value == other.max_value
        )


@deconstructible
class CharFieldValidator:
    """Initialize the validator with a maximum length for the character field."""

    def __init__(self, max_length):
        """Initialize the validator with a specified maximum length."""
        self.max_length = max_length
        self.validator = MaxLengthValidator(max_length)

    def __call__(self, value):
        """Validate the value if it's not empty."""
        if not value:
            return None
        return self.validator(value)

    def __eq__(self, other):
        """Check equality with another validator."""
        return isinstance(other, CharFieldValidator) and self.max_length == other.max_length
