set1_countries = {'USA', 'Indonesia', 'Australia', 'Germany','Netherlands','Italy','Spain','France','United Kingdom'}
set2_countries = {'Brazil', 'France', 'India', 'Japan'}

passport_name = input("Enter a country name of the passport holder: ")
destination_name = input("Enter a destination country name :")
country_name = input("Enter a Trasnit country name :")

if country_name in set1_countries:
    print("Transit Visa Required")
elif country_name in set2_countries:
    print("Transit visa Not Requried")
else:
    print("Country not found in either set")
