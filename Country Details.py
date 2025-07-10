from countryinfo import CountryInfo

country = CountryInfo(input("Country: "))


print(f"Capital: {country.capital()}")
print(f"Population: {country.population()}")
print(f"Area (square km): {country.area()}")
print(f"Region: {country.region()}")
print(f"Demonym: {country.demonym()}")
print(f"Currency: {country.currencies()}")
print(f"Languages: {country.languages()}")
print(f"Borders: {country.borders()}")