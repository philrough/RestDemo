from db import countries

class server:


    def refresh_data():
        countries = db.countries
        return max(country["id"] for country in countries) + 1

    def find_next_id():
        return max(country["id"] for country in countries) + 1
	
    def find_country_by_name(name):
        for country in countries:
            if country["name"] == name:
                return country["id"] -1
        return 0

    def find_country_by_capital(capital):
        for country in countries:
            if country["capital"] == capital:
                return country["id"] -1
        return 0

    def find_countryname_by_capital(capital):
        for country in countries:
            if country["capital"] == capital:
                return country["name"]
        return "Error"
	
    def find_capitalname_by_country(name):
        for country in countries:
            if country["name"] == name:
                return country["capital"]
        return "Error"
