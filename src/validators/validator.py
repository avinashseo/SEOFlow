class Validator:
    """
    Base validation class.

    Every validator returns:

    errors

    warnings

    info
    """

    def validate(self):
        raise NotImplementedError

        