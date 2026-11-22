HIGH_THRESHOLD = 0.6
MEDIUM_THRESHOLD = 0.3


def calculate_risk(income, debt, age):
    """Retourne HIGH, MEDIUM ou LOW, ou -1 si le revenu est invalide."""
    if age < 0:
        raise ValueError("age must be non-negative")
    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > HIGH_THRESHOLD:
        return "HIGH"
    if ratio > MEDIUM_THRESHOLD:
        return "MEDIUM"
    return "LOW"