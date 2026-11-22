import pytest
from credit import calculate_risk


def test_high_risk():
    assert calculate_risk(1000, 700, 30) == "HIGH"


def test_medium_risk():
    assert calculate_risk(1000, 400, 30) == "MEDIUM"


def test_low_risk():
    assert calculate_risk(1000, 100, 30) == "LOW"


def test_zero_income():
    assert calculate_risk(0, 100, 30) == -1


def test_negative_income():
    assert calculate_risk(-500, 100, 30) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0, 30) == "LOW"


def test_ratio_exactly_0_3():
    assert calculate_risk(1000, 300, 30) == "LOW"


def test_ratio_exactly_0_6():
    assert calculate_risk(1000, 600, 30) == "MEDIUM"


def test_negative_age():
    with pytest.raises(ValueError):
        calculate_risk(1000, 100, -1)