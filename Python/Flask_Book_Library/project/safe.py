class SafeValue:
    """A type wrapper that doesn't show its content in str(), format() or repr().
    """
    def __init__(self, value):
        type(value).__init__(value)

    def __format__(self, _spec):
        return "****"

    def __str__(self):
        return "****"

    def __repr__(self):
        return "****"
