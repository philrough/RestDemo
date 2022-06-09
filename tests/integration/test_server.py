from server import server
import pytest

def test_find_next_id():
    # Act
    response = server.find_next_id()

    # Assert
    assert response == 5


def test_find_country_by_name():
    # Act
    response_id = server.find_country_by_name("Egypt")

    # Assert
    assert response_id == 3


def test_find_country_by_invalid_name():
    # Act
    response_id = server.find_country_by_name("France")

    # Assert
    assert response_id == 0


def test_find_country_by_capital():
    # Act
    response_id = server.find_country_by_capital("Cairo")

    # Assert
    assert response_id == 3


def test_find_country_by_invalid_capital():
    # Act
    response_id = server.find_country_by_capital("Paris")

    # Assert
    assert response_id == 0


def test_find_countryname_by_capital():
    # Act
    response = server.find_countryname_by_capital("Cairo")

    # Assert
    assert response == "Egypt"


def test_find_countryname_by_invalid_capital():
    # Act
    response = server.find_countryname_by_capital("Paris")

    # Assert
    assert response == "Error"


def test_find_capitalname_by_country():
    # Act
    response = server.find_capitalname_by_country("Egypt")

    # Assert
    assert response == "Cairo"


def test_find_capitalname_by_invalid_country():
    # Act
    response = server.find_capitalname_by_country("France")

    # Assert
    assert response == "Error"

