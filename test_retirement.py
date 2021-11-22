import pytest
from datetime import datetime
from retirement import time_until_full_retirement
from pytest_bdd import scenario, given, when, then


@scenario('retirement.feature', 'Calculates Retirement')
@pytest.mark.parametrize("test_input,result", [
	('02/1993', (67, 0)), ('07/1942', (66, 0)), ('11/1962', (67, 0))])
def test_retirement(test_input, result):
	year, months, date = time_until_full_retirement(datetime.strptime(test_input, "%m/%Y"))
	assert (result[0] == year and result[1] == months)


@scenario('retirement.feature', 'Invalid Date')
@pytest.mark.parametrize("test_input,result", [
	('02/2022', (67, 0))])
def test_invalid_date(test_input, result):
	year, months, date = time_until_full_retirement(datetime.strptime(test_input, "%m/%Y"))
	assert (result[0] == year and result[1] == months)
