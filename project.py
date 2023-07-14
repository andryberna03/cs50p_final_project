"""
    AUTHOR:
    Andrea Bernardo
    Fano, Italy
    https://www.linkedin.com/in/ab2003-andrea-bernardo/
    https://github.com/andryberna03
"""


import requests
from tabulate import tabulate
import re
import datetime
import sys
import random
import cowsay


def main():
    location, language, temperature_unit = ask_information()
    latitute, longitude = take_lat_and_lon(location)

    real_time_insights: list[list[str]] = find_current_weather(latitute, longitude, language, temperature_unit)
    print_weather_table(real_time_insights)

    answer_forecast: tuple[str, str] = ask_for_insights('forecast')
    if answer_forecast == 'Yes':
        forecast_insights: list[list[str]] = find_forecast(latitute, longitude, language, temperature_unit)
        print_forecast_table(forecast_insights)

    answer_pollution: tuple[str, str] = ask_for_insights('pollution')
    if answer_pollution == 'Yes':
        end_date: str = take_end_date_pollution()
        pollution_avarage: str = find_pollution_avarage(latitute, longitude, end_date)
        print(f'The pollution avarage of the time span from 2020-11-27 untill your choosen date, according AQI (Air Quality Index), is {pollution_avarage}')


def ask_information() -> list[str]:
    """
        Collect useful information, such as location, language and temperature unit,
        from the user in order to use them in further functions

        :return: A list of str containing checked location, language and temperature unit entered by the user
    """

    input_stage = 'location'

    if input_stage == 'location':
        control_loop_location: bool = True
        while control_loop_location:
            location: str = input('Whose capital would you like to know about the weather? ').strip().title()
            location_checked: bool = check_location(location)
            if location_checked == True:
                right_location: str = location
                input_stage = 'language'
                control_loop_location: bool = False

    if input_stage == 'language':
        control_loop_language: bool = True
        while control_loop_language:
            language: str = input('What language do you prefer to have weather knowledge in? ').strip().title()
            language_checked: tuple[bool,str] = check_language(language)
            if language_checked[0] == True:
                right_language: str = language_checked[1]
                input_stage = 'temperature_unit'
                control_loop_language: bool = False

    if input_stage == 'temperature_unit':
        control_loop_temperature_unit: bool = True
        while control_loop_temperature_unit:
            temperature_unit: str = input('What unit of temperature measurement are you used to using? (Celsius/Fahrenheit/Kelvin) ').strip().title()
            temperature_unit_checked: tuple[bool,str] = check_temperature_units(temperature_unit)
            if temperature_unit_checked[0] == True:
                right_temperature_unit: str = temperature_unit_checked[1]
                control_loop_temperature_unit: bool = False
 
    return [right_location, right_language, right_temperature_unit]


def check_location(location: str) -> bool:
    """
        Check if the entered location by the user is inside the capitals of the world' list

        :param location: Entered location by the user

        :return: A bool indicating if the location is inside the capitals of the world
    """

    capitals: list[str] = [
        "Abuja",
        "Accra",
        "Addis Ababa",
        "Algiers",
        "Amman",
        "Amsterdam",
        "Andorra la Vella",
        "Antananarivo",
        "Apia",
        "Ashgabat",
        "Asmara",
        "Asuncion",
        "Athens",
        "Baghdad",
        "Baku",
        "Bamako",
        "Bandar Seri Begawan",
        "Bangkok",
        "Bangui",
        "Banjul",
        "Basseterre",
        "Beijing",
        "Beirut",
        "Belgrade",
        "Belmopan",
        "Berlin",
        "Bern",
        "Bishkek",
        "Bissau",
        "Bogota",
        "Brasilia",
        "Bratislava",
        "Bridgetown",
        "Brussels",
        "Bucharest",
        "Budapest",
        "Buenos Aires",
        "Cairo",
        "Canberra",
        "Caracas",
        "Cardiff",
        "Castries",
        "Chisinau",
        "Conakry",
        "Copenhagen",
        "Dakar",
        "Damascus",
        "Dodoma",
        "Djibouti",
        "Dili",
        "Djibouti",
        "Doha",
        "Dublin",
        "Dushanbe",
        "Edinburgh",
        "Funafuti",
        "Georgetown",
        "Guatemala City",
        "Hanoi",
        "Harare",
        "Helsinki",
        "Honiara",
        "Islamabad",
        "Jakarta",
        "Jerusalem",
        "Kabul",
        "Kampala",
        "Kathmandu",
        "Khartoum",
        "Kiev or Kiev",
        "Kingston",
        "Kingstown",
        "Kinshasa",
        "Kotte",
        "Kuala Lumpur",
        "Kuwait City",
        "Kyiv or Kiev",
        "La Paz",
        "Libreville",
        "Lilongwe",
        "Lisbon",
        "Ljubljana",
        "London",
        "Lome",
        "Lusaka",
        "Luxembourg",
        "Madrid",
        "Majuro",
        "Malabo",
        "Male",
        "Maseru",
        "Mbabana",
        "Mexico City",
        "Minsk",
        "Mogadishu",
        "Monaco",
        "Monrovia",
        "Montevideo",
        "Moroni",
        "Moscow",
        "Muscat",
        "N'Djamena",
        "Nairobi",
        "Nassau",
        "Nay Pyi Taw",
        "New Delhi",
        "Niamey",
        "Nicosia",
        "Nouakchott",
        "Nuku'alofa",
        "Ottawa",
        "Ouagadougou",
        "Palikir",
        "Panama City",
        "Paramaribo",
        "Paris",
        "Phnom Penh",
        "Podgorica",
        "Port au Prince",
        "Port Moresby",
        "Port of Spain",
        "Port Vila",
        "Porto Novo",
        "Praia",
        "Cape Town",
        "Pyongyang",
        "Quito",
        "Rabat",
        "Reykjavik",
        "Riga",
        "Riyadh",
        "Rome",
        "Roseau",
        "Saint George's",
        "Saint John's",
        "San Jose",
        "San Marino",
        "San Salvador",
        "Sana'a",
        "Santiago",
        "Santo Domingo",
        "Sao Tome",
        "Seoul",
        "Skopje",
        "Sofia",
        "Sri Jayawardenapura Kotte",
        "Stockholm",
        "Sucre",
        "Suva",
        "T'aipei",
        "Tallinn",
        "Tarawa Atoll",
        "Tashkent",
        "Tbilisi",
        "Tegucigalpa",
        "Teheran",
        "Thimphu",
        "Tirane",
        "Tokyo",
        "Tripoli",
        "Tunis",
        "Ulaanbaatar",
        "Vaduz",
        "Valletta",
        "Vatican City",
        "Victoria",
        "Vienna",
        "Vientiane",
        "Vilnius",
        "Warsaw",
        "Wellington",
        "Windhoek",
        "Yaounde",
        "Yamoussoukro",
        "Yerevan",
        "Zagreb",
        "Zurich"
    ]

    check_result: bool = False

    if location == '0':
        easter_egg()
    elif location not in capitals:
        print(f'Please, enter one of the following capitals: {capitals}')
    else:
        check_result: bool = True

    return check_result


def check_language(language: str) -> tuple[bool,str]:
    """
        Check if the entered language by the user is inside the languages of the world

        :param language: Entered language by the user

        :return: A tuple indicating if the language is inside the languages of the world in bool form and the related language's code in str form
    """

    languages: dict = {
        "Afrikaans": "af",
        "Albanian": "al",
        "Arabic": "ar",
        "Azerbaijani": "az",
        "Bulgarian": "bg",
        "Catalan": "ca",
        "Czech": "cz",
        "Danish": "da",
        "German": "de",
        "Greek": "el",
        "English": "en",
        "Basque": "eu",
        "Persian (Farsi)": "fa",
        "Finnish": "fi",
        "French": "fr",
        "Galician": "gl",
        "Hebrew": "he",
        "Hindi": "hi",
        "Croatian": "hr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "kr",
        "Latvian": "la",
        "Lithuanian": "lt",
        "Macedonian": "mk",
        "Norwegian": "no",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Português Brasil": "pt_br",
        "Romanian": "ro",
        "Russian": "ru",
        "Swedish": "sv",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Spanish": "sp",
        "Serbian": "sr",
        "Thai": "th",
        "Turkish": "tr",
        "Ukrainian": "ua",
        "Vietnamese": "vi",
        "Chinese Simplified": "zh_cn",
        "Chinese Traditional": "zh_tw",
        "Zulu": "zu"
    }

    check_result: bool = (False, None)

    if language == '0':
        easter_egg()
    elif language not in languages.keys():
        print(f'Please, enter one of the following languages: {list(languages.keys())}')
    else:
        check_result: bool = (True, languages[language])
    
    return check_result


def check_temperature_units(temperature_unit: str) -> tuple[bool,str]:
    """
        Check if the entered temperature unit by the user is inside the temperature units' dict

        :param temperature_unit: Entered temperature unit by the user

        :return: A tuple indicating if the temperature unit is inside the temperature units' dict in bool form and the related temperature unit's code in str form
    """

    temperature_units: dict = {
        'Celsius':'metric',
        'Fahrenheit':'imperial',
        'Kelvin':'standard'
    }

    check_result: tuple[bool,str] = (False, None)

    if temperature_unit == '0':
        easter_egg()
    elif temperature_unit not in temperature_units.keys():
        print(f'Please, enter one of the following temperature measurement: {list(temperature_units.keys())}')
    else:
        check_result: tuple[bool,str] = (True, temperature_units[temperature_unit])

    return check_result


def take_lat_and_lon(location: str) -> tuple[str,str]:
    """
        Collect latitute and longitude of the entered location by the user 
        through an OpenWeather API in order to use them in further functions

        :param location: Entered location by the user

        :return: A tuple containing latitute and longitude of the entered location by the user in str form
    """

    location_api: requests.models.Response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=&appid=07403ffde4424fffa4638e9984caeec9")

    lat: str = location_api.json()[0]['lat']
    lon: str = location_api.json()[0]['lon']

    return (lat, lon)


def find_current_weather(lat: str, lon: str, lang: str, temp_unit: str) -> list[list[str]]:
    """
        Collect the current weather relevant information through an OpenWeather API 
        in order to use them in further functions:
          - weather type
          - weather description
          - feels like temperature
          - max temperature 
          - min temperature

        :param lat: Latitude retrieved by the entered location by the user
        :param lon: Longitude retrieved by the entered location by the user
        :param lang: Language retrieved by the entered langugae by the user
        :param temp_unit: Temperature unit retrieved by the entered temperature unit by the user

        :return: a list of list containing all the information collected through an OpenWeather API in str form
    """
    
    current_weather_api: requests.models.Response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={temp_unit}&lang={lang}&appid=07403ffde4424fffa4638e9984caeec9")

    current_weather_insights: list[list[str]] = [
        ['Wheater', current_weather_api.json()['weather'][0]['main']],
        ['Short weather description', current_weather_api.json()['weather'][0]['description']],
        ['Feels like temperature', current_weather_api.json()['main']['feels_like']],
        ['Maximum temperature', current_weather_api.json()['main']['temp_max']],
        ['Minimum temperature', current_weather_api.json()['main']['temp_min']]
    ]

    return current_weather_insights


def print_weather_table(insights: list[list[str]]) -> None:
    """
        Print a table with the current weather information previously obtained through an OpenWeather API
        of the entered location by the user

        :param insights: A list of list containing all the information collected through an OpenWeather API
    """

    # Just for aesthetics reasons I wanted to update this list item in its version with the first letter of the first word capitalized
    for info in insights:
        if 'description' in info[0]:
            new_description: str = info[1].capitalize()
            info[1] = new_description

    print(tabulate(insights, tablefmt="rounded_grid"))


def ask_for_insights(question_type: str) -> str:
    """
        Understand if the user wants further information about the weather

        :param question_type: A str that leads to a specific question and related checking

        :return: A str containing the checked anwser entered by the user
    """

    control_loop: bool = True

    if question_type == 'forecast':
            while control_loop:
                answer: str = input('Interested in knowing what the weather will be like in the next 5 days? (Yes/No) ').strip().title()
                checked_answer_forecast: bool = check_answer_insights(answer)

                if checked_answer_forecast == control_loop:
                    control_loop: bool = False

    if question_type == 'pollution':
        while control_loop:
                answer: str = input('Do you wish to have the average level of air pollution in the last period? (Yes/No) ').strip().title()
                checked_answer_pollution: bool = check_answer_insights(answer)

                if checked_answer_pollution == control_loop:
                    control_loop: bool = False

    return answer


def check_answer_insights(answer: str) -> bool:
    """
        Check if the entered answer by the user is in the correct format

        :param answer: A str that contains the entered answer by the user

        :return: A bool indicating if the entered answer by the user is in the correct format
    """

    check_answer: bool = True

    if answer == '0':
        easter_egg()
    elif answer != 'Yes' and answer != 'No':
        print(f'Please, enter "Yes" or "No"')
        check_answer: bool = False

    return check_answer


def find_forecast(lat: str, lon: str, lang: str, temp_unit: str) -> list[list[str]]:
    """
        Collect the current weather relevant information through an OpenWeather API 
        in order to use them in further functions:
          - weather type
          - weather description
          - feels like temperature
          - max temperature 
          - min temperature

        :param lat: Latitude retrieved by the entered location by the user
        :param lon: Longitude retrieved by the entered location by the user
        :param lang: Language retrieved by the entered langugae by the user
        :param temp_unit: Temperature unit retrieved by the entered temperature unit by the user

        :return: A list of lists containing all the information collected through an OpenWeather API in str form
    """

    forecast_weather_api: requests.models.Response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={temp_unit}&lang={lang}&appid=07403ffde4424fffa4638e9984caeec9")

    forecasted_weather: list = list()

    for dict_index in range(40):
        forecasted_weather.append([
            forecast_weather_api.json()['list'][dict_index]['dt_txt'],
            forecast_weather_api.json()['list'][dict_index]['weather'][0]['main'],
            forecast_weather_api.json()['list'][dict_index]['weather'][0]['description'],
            forecast_weather_api.json()['list'][dict_index]['main']['feels_like'],
            forecast_weather_api.json()['list'][dict_index]['main']['temp_max'],
            forecast_weather_api.json()['list'][dict_index]['main']['temp_min']
        ])

    return forecasted_weather


def print_forecast_table(insights) -> None:
    """
        Print a table with the forecast weather information previously obtained through an OpenWeather API
        of the entered location by the user

        :param insights: A list of lists containing all the information collected through an OpenWeather API in str form
    """

    # Just for aesthetics reasons I wanted to update this list item in its version with the first letter of the first word capitalized
    for info in insights:
        new_description: str = info[2].capitalize()
        info[2] = new_description

    headers: list[str] = ["", 'Wheater', "Short weather description", 'Feels like temperature', 'Maximum temperature', 'Minimum temperature']
    print(tabulate(insights, headers, tablefmt="fancy_grid"))


def take_end_date_pollution() -> str:
    """
        Collect a date from the user in order to use it in further functions

        :return: A str containing a checked date entered by user
    """

    control_loop: bool = True

    while control_loop:
        end_day: str = input('Enter the date up to which you are interested in learning about the average level of air pollution (yyyy-mm-dd format after 2020-11-26): ').strip()

        checked_end_date_format = check_end_date_format(end_day)
        if checked_end_date_format:
            checked_end_day_not_later_than_current_date: bool = check_not_later_than_current_date(end_day)
            if checked_end_day_not_later_than_current_date:
                checked_end_day_no_earlier_than_2020_11_26: bool = check_not_earlier_than_2020_11_27(end_day)
                if checked_end_day_no_earlier_than_2020_11_26:
                    checked_end_day: str = end_day
                    control_loop: bool = False
                else:
                    print("Please, insert a date after 2020-11-26")
            else:
                print("Please, insert a date not later than current date")
        else:
            print("Please, insert a date in the format 'yyyy-mm-dd'")

    return checked_end_day


def check_end_date_format(end_day: str) -> bool:
    """
        Check if the entered date by the user is in the format 'yyyy-mm-dd'

        :param end_day: A str that contains the entered date by the user

        :return: A True or False indicating if the entered date by the user is in the format 'yyyy-mm-dd'
    """

    check_date: bool = False

    if end_day == '0':
        easter_egg()
    elif re.match(r'^([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])$', end_day):
        check_date: bool = True

    return check_date


def check_not_later_than_current_date(end_day: str) -> bool:
    """
        Check if the entered date by the user is not later than current date

        :param end_day: A str that contains the entered date by the user

        :raise ValueError: If end_day doesn't match the indicated format in .strptime()

        :return: A True or False indicating if the entered date by the user is not later than current date
    """

    try:
        current_date: datetime.date = datetime.date.today()
        datetime_user: datetime.date = datetime.datetime.strptime(end_day, "%Y-%m-%d").date()

        check_date: bool = True

        if datetime_user > current_date:
            check_date: bool = False

    except ValueError:
        check_date: bool = False

    return check_date


def check_not_earlier_than_2020_11_27(end_day: str) -> bool:
    """
        Check if the entered date by the user is not earlier than 2020-11-27

        :param end_day: A str that contains the entered date by the user

        :return: A bool indicating if the entered date by the user is not earlier than 2020-11-27
    """

    datetime_limit: datetime.date = datetime.datetime.strptime('2020-11-26', "%Y-%m-%d").date()
    datetime_user: datetime.date = datetime.datetime.strptime(end_day, "%Y-%m-%d").date()

    check_date: bool = True

    if datetime_limit >= datetime_user:
        check_date: bool = False

    return check_date


def find_pollution_avarage(lat: str, lon: str, end_date: str) -> str:
    """
        Collect the pollution AQI (Air Quality Index) through an OpenWeather API and
        compute the avarage of the AQI

        :param lat: Latitude retrieved by the entered location by the user
        :param lon: Longitude retrieved by the entered location by the user
        :param end_date: Language retrieved by the entered langugae by the user

        :return: A str containing the pollution avarage of the selected time span
    """

    end_date_splitted: list = end_date.split('-')
    date_end: datetime.datetime = datetime.datetime(int(end_date_splitted[0]), int(end_date_splitted[1]), int(end_date_splitted[2]))
    unix_time_end: int = int(date_end.timestamp())

    pollution_api: requests.models.Response = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start=1606431600&end={unix_time_end}&appid=07403ffde4424fffa4638e9984caeec9')

    pollution_values: dict = {
                1: 'GOOD',
                2: 'FAIR',
                3: 'MODERATE',
                4: 'POOR',
                5: 'VERY POOR'
    }

    pollution_score: int = sum(entry['main']['aqi'] for entry in pollution_api.json()['list'])
    pollution_average: int = round(pollution_score / len(pollution_api.json()['list']))

    pollution_average_description: str = pollution_values.get(pollution_average)

    return pollution_average_description


def easter_egg() -> None:
    characters: list = [
        'cow',
        'dragon',
        'fox',
        'ghostbusters',
        'kitty',
        'meow',
        'stegosaurus',
        'trex',
        'turkey',
        'turtle',
        'tux'
    ]
 
    character: str = random.choice(characters)

    sys.exit(cowsay.get_output_string(character, 'Since you entered 0 it shows that you are a real programmer, so enjoy this easter egg!'))


if __name__ == "__main__":
    main()