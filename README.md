# WEATHER'S INFORMATION
WEATHER'S INFORMATION is Andrea Bernardo's Python final project for Harvard University Online Open Course CS50P. It is a computer science course on introduction to programming with Python.

#### Video Demo: <https://youtu.be/mI7wj3iifr8>

## REQUIRMENTS:

**_requests_**: It is a HTTP library that allows to send HTTP/1.1 requests without manually add queries or form-encode PUT & POST data.

**_tabulate_**: This is a table library that is able to present mixed textual and numeric data in a simple and readable manner with formatting driven by the data itself.

**_re_**: This is a module that provides regular expression matching operations and it is built-in Python itself.

**_datetime_**: It is a module built-in Python itself that supports manipulation of dates and times.

**_sys_**: This module gives a strong inteaction with Python interpreter and it is built-in Python itself.

**_random_**: A built-in Python module that provides pseudo-random generations.

**_cowsay_**: A library of ascii art that enables different characters to communicate.

## DESCRIPTION:
WEATHER'S INFORMATION contains exaclty four files. This **README.md**, which has the aim to explain my project, a **requirements.txt**, that list, one per line, all libraries that my project requires, a **project.py**, wherein is present the entire code, and a **test_project.py**, whom has useful pytest for testing my project.

### _What will my software do?_

The objective of this program is to provide the user with relevant information related to the weather in one of the world's capitals. This information can also be provided in different languages and with different units of measurement.

Weather information are divided into three categories: current weather, weather forecast, and air pollution. These are shown to the user in the order listed, but with one difference: the first category is always provided to the user, while the other two are available only if the user explicitly requests them.

### _How will it be executed?_

For this program, command line arguments are not necessary, since specific inputs will be requested from the user when needed. The first inputs are the _capital city_ whose weather he is interested in knowing, the _language_ in which he wants to know the weather, and _units of measurement_ he is used to using for temperature values.

After showing a table with the initial data and specifications of the initial inputs, we move on to ask the user if interested in more information regarding the weather. In case of no, the program will jump to the next step, otherwise it will continue with the weather forecast for the 5 days following the current one. The user's initial inputs are reused at this stage so as to provide him with weather forecasts from the same capital, in the same language, and with the same unit of measurement.

Finally, after showing a table with the weather forecast for the next 5 days following the specifications of the first inputs we move on to ask the user if interested again in having more information regarding the weather. In case of no the program will stop, otherwise it will continue with the average value of air pollution in a defined time frame. This time frame is from 2020-11-27, the first day in which the data are available, to the date that the user provides. Only the initial input involving the capital city will be used at this time. The program will end by showing the average level of air pollution according to the AQI, or air quality index.

To better understand what I would like to explain here is a **_beautiful GIF_** with the code in action:

![Alt text](<CS50P final project functioning.gif>)

## DESIGN CHOICES:
The information that are shown to the user, both tabular and non-tabular, is taken from the website <https://openweathermap.org> via APIs, namely Application Programming Interface. I chose this site because it is among the most famous regarding data on history weather, current weather, and weather forecasts.

As for the actual design of the code, I wanted to create general functions, such as _ask_information()_, and then place secondary functions within them to check inputs, for an example, _check_temperature_units()_. All general functions are called in the main, while secondary functions are called at the useful time in the general functions.

As for fixing code problems, however, the checking of user-entered dates is done sequentially and that I had to use a dedicated method to sum up all the AQIs of air pollution. In the former, the first check focused on the date format, then the second whether the date is later than the current date, and then the third whether it is earlier than the date when the data began to be available, i.e., 2020-11-27. In the latter, I had to use the class method _sum()_ in such a way as to make the code faster, because of the large amount of data to scan, and I chose that one because it was written in C language instead of Python language

In the end, in  **_test_project.py_** I created tests only for the input check functions, this is because they were the only testable functions, and I tried to include multiple tests covering all possible cases. The only input check function that I did not test is _check_not_later_than_current_date()_ since it is not possible to make the local variable _current date_ fixed since it is generated by a class method of the **_datetime_** library.

## AUTHOR: 
Andrea Bernardo, italian born in 2003, currently undergraduate student in Digital Management in  Department of Management at Ca' Foscari University of Venice, Italy, Class of 2025 

<https://www.linkedin.com/in/ab2003-andrea-bernardo/>

<https://github.com/andryberna03>