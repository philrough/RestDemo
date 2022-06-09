import app
import requests

def test_get_countries():
    # Arrange
    url = "http://127.0.0.1:8080/countries"
    
    # Act
    response = requests.get(url)
    data = eval(response.text)
    
    # Assert
    assert response.status_code == 200

    assert len(data) >= 4

    assert data[1]["capital"] == "Bangkok"
    assert data[2]["capital"] == "Canberra"
    assert data[3]["capital"] == "Cairo"

def test_get_country():
    # Arrange
    url = "http://127.0.0.1:8080/country"
    
    # Act
    response = requests.get(url)
    data = response.json()
    
    # Assert
    assert response.status_code == 200

    assert len(data) == 4

    assert data["area"] == 513120
    assert data["capital"] == "Bangkok"
    assert data["name"] == "Thailand"
    assert data["id"] == 2

def test_get_country_by_id():
    # Arrange
    url = "http://127.0.0.1:8080/country/2"
    
    # Act
    response = requests.get(url)
    data = response.json()
    
    # Assert
    assert response.status_code == 200

    assert len(data) == 4

    assert data["area"] == 7617930
    assert data["capital"] == "Canberra"
    assert data["name"] == "Australia"
    assert data["id"] == 3

def test_get_country_by_name():
    # Arrange
    url = "http://127.0.0.1:8080/country/Egypt"
    
    # Act
    response = requests.get(url)
    data = response.json()
    
    # Assert
    assert response.status_code == 200

    assert len(data) == 4

    assert data["area"] == 1010408
    assert data["capital"] == "Cairo"
    assert data["name"] == "Egypt"
    assert data["id"] == 4

def test_get_country_by_capital():
    # Arrange
    url = "http://127.0.0.1:8080/capital/Cairo"
    
    # Act
    response = requests.get(url)
    data = response.json()
    
    # Assert
    assert response.status_code == 200

    assert len(data) == 4

    assert data["area"] == 1010408
    assert data["capital"] == "Cairo"
    assert data["name"] == "Egypt"
    assert data["id"] == 4

def test_get_capital_name_by_country():
    # Arrange
    url = "http://127.0.0.1:8080/capital/bycountry/Egypt"
    
    # Act
    response = requests.get(url)
    
    # Assert
    assert response.status_code == 200

    assert len(response.text) == 5

    assert response.text == "Cairo"

def test_get_country_name_by_capital():
    # Arrange
    url = "http://127.0.0.1:8080/country/bycapital/Cairo"
    
    # Act
    response = requests.get(url)
    
    # Assert
    assert response.status_code == 200

    assert len(response.text) == 5

    assert response.text == "Egypt"


def test_add_country():
    # Arrange
    url = "http://127.0.0.1:8080/add/country"

    # Act
    response = requests.post(url,
        json = {"name": "Germany", "capital": "Berlin", "area": 999999}
     )
    data = response.json()
    
    # Assert
    assert response.status_code == 201

    assert data["name"] == "Germany"


def test_add_country_with_invalid_body():
    # Arrange
    url = "http://127.0.0.1:8080/add/country"

    # Act
    response = requests.post(url,
        # json = {"name": "Germany", "capital": "Berlin", "area": 999999}
     )
    data = response.json()
    
    # Assert
    assert response.status_code == 415

    assert '"error":"Request must be JSON"' in response.text
