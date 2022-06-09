import requests
import pytest
import app as app


def test_get_counties(): 
    # Act
    response = app.get_countries() 
    data = eval(response)           

    # Assert
    assert data[0]["area"] == 000000
    assert data[0]["capital"] == "Error"
    assert data[0]["name"] == "Error"
    assert data[0]["id"] == 1


def test_get_country():
    # Act
    response = app.get_country()
    
    # Assert
    assert response["area"] == 513120
    assert response["capital"] == "Bangkok"
    assert response["name"] == "Thailand"
    assert response["id"] == 2


def test_get_country_by_id():
    # Act
    response = app.get_country_by_id(0)
    
    # Assert
    assert response["area"] == 000000
    assert response["capital"] == "Error"
    assert response["name"] == "Error"
    assert response["id"] == 1


def test_get_country_by_name():
    # Act
    response = app.get_country_by_name("Error")
    
    # Assert
    assert response["area"] == 000000
    assert response["capital"] == "Error"
    assert response["name"] == "Error"
    assert response["id"] == 1


def test_get_capital_by_country(requests_mock):
    # Arrange
    url = "http://127.0.0.1:8080/country/Egypt"
    
    # Act
    requests_mock.get(url, json = {"area":12345678,"capital":"London","id":5,"name":"England"})
    response = requests.get(url)
    data = response.json()
    
    # Assert
    assert response.status_code == 200

    assert len(data) == 4

    assert data["area"] == 12345678
    assert data["capital"] == "London"
    assert data["name"] == "England"
    assert data["id"] == 5


def test_get_country_by_capital(requests_mock):
    # Arrange
    url = "http://127.0.0.1:8080/capital/Cairo"
    
    # Act
    requests_mock.get(url, json = {"area":12345678,"capital":"London","id":5,"name":"England"})
    response = requests.get(url)
    data = response.json()
    
    # Assert
    assert response.status_code == 200

    assert len(data) == 4

    assert data["area"] == 12345678
    assert data["capital"] == "London"
    assert data["name"] == "England"
    assert data["id"] == 5


def test_get_country_name_by_capital(requests_mock):
    # Arrange
    url = "http://127.0.0.1:8080/country/bycapital/Cairo"
    
    # Act
    requests_mock.get(url, json = "England")
    response = requests.get(url)
    
    # Assert
    assert response.status_code == 200

    assert response.text == '"England"'


def test_get_capital_name_by_country(requests_mock):
    # Arrange
    url = "http://127.0.0.1:8080/capital/bycountry/Egypt"
    
    # Act
    requests_mock.get(url, json = "London")
    response = requests.get(url)
    
    # Assert
    assert response.status_code == 200

    assert response.text == '"London"'


def test_get_country_by_id():
    # Act
    response = app.get_country_by_id(0)
    
    # Assert
    assert response["area"] == 000000
    assert response["capital"] == "Error"
    assert response["name"] == "Error"
    assert response["id"] == 1


def test_get_country_by_name_method_mock(mocker):
    # Act
    mocker.patch("server.server.find_country_by_name",
        return_value = 0)
    
    response = app.get_country_by_name("Egypt")
    
    # Assert
    assert response["area"] == 000000
    assert response["capital"] == "Error"
    assert response["name"] == "Error"
    assert response["id"] == 1


def test_get_country_by_capital_method_mock(mocker):
    # Act
    mocker.patch("server.server.find_country_by_capital",
        return_value = 0)
    
    response = app.get_country_by_capital("Cairo")
    
    # Assert
    assert response["area"] == 000000
    assert response["capital"] == "Error"
    assert response["name"] == "Error"
    assert response["id"] == 1


def test_get_country_name_by_capital_method_mock(mocker):
    # Act
    mocker.patch("server.server.find_countryname_by_capital",
        return_value = "England")
    response = app.get_country_name_by_capital("Cairo")
    
    # Assert
    assert response == "England"

def test_get_capital_name_by_country_method_mock(mocker):
    # Act
    mocker.patch("server.server.find_capitalname_by_country",
        return_value = "London")
    response = app.get_capital_name_by_country("Egypt")
    
    # Assert
    assert response == "London"




