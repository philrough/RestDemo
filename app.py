# app.py
from flask import Flask, jsonify, request
from flask import current_app as app
from server import server
from db import countries



app = Flask(__name__)

@app.get("/countries")
def get_countries():
    return str(countries)
	
@app.get("/country")
def get_country():
    return countries[1]
	
@app.get("/country/<int:id>")
def get_country_by_id(id):
    return countries[id]
	
@app.get("/country/<string:name>")
def get_country_by_name(name):
    return countries[server.find_country_by_name(name)]

@app.get("/capital/<string:capital>")
def get_country_by_capital(capital):
    return countries[server.find_country_by_capital(capital)]
	
@app.get("/country/bycapital/<string:capital>")
def get_country_name_by_capital(capital):
    return (server.find_countryname_by_capital(capital))
	
@app.get("/capital/bycountry/<string:name>")
def get_capital_name_by_country(name):
    return (server.find_capitalname_by_country(name))
	
@app.post("/add/country")
def add_country():
    breakpoint()
    if request.is_json:
        country = request.get_json()
        country["id"] = server.find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
