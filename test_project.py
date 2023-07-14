import project

def test_check_location():
    assert project.check_location('Boston') == False
    assert project.check_location('cjrovjkirh') == False
    assert project.check_location('0438') == False
    assert project.check_location(' ') == False
    assert project.check_location(3849) == False
    assert project.check_location('Libreville') == True


def test_check_language():
    assert project.check_language('ancjnrbr') == (False, None)
    assert project.check_language('4094838') == (False, None)
    assert project.check_language(' ') == (False, None)
    assert project.check_language(462904) == (False, None)
    assert project.check_language('Macedonian') == (True, 'mk')


def test_check_temperature_units():
    assert project.check_temperature_units('cnducneiv') == (False, None)
    assert project.check_temperature_units('73849') == (False, None)
    assert project.check_temperature_units(' ') == (False, None)
    assert project.check_temperature_units(93749) == (False, None)
    assert project.check_temperature_units('Fahrenheit') == (True, 'imperial')


def test_take_lat_and_lon():
    assert project.take_lat_and_lon('Lilongwe') == (-13.9875107, 33.768144)
    assert project.take_lat_and_lon('Honiara') == (-9.4310769, 159.9552552)


def test_check_answer_insights():
    assert project.check_answer_insights('cjriviuvr') == False
    assert project.check_answer_insights('624834') == False
    assert project.check_answer_insights(' ') == False
    assert project.check_answer_insights(28948) == False
    assert project.check_answer_insights('Yes') == True
    assert project.check_answer_insights('No') == True


def test_check_end_date_format():
    assert project.check_end_date_format('48390-238-483') == False
    assert project.check_end_date_format('203-2-4') == False
    assert project.check_end_date_format('abcd-ef-gh') == False
    assert project.check_end_date_format(' ') == False
    assert project.check_end_date_format('2020-12-12') == True
    assert project.check_end_date_format('4830-39-70') == True


def test_check_not_earlier_than_2020_11_27():
    assert project.check_not_earlier_than_2020_11_27('1990-04-25') == False
    assert project.check_not_earlier_than_2020_11_27('2022-07-09') == True