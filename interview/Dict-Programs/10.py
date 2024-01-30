# Handling missing keys in Python dictionaries.
country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}
for key,value in country_code.items():
    print(f"{key}-->{value}")