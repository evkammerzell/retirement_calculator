# Team 5's Testing on Team 6 Solution
# CSC 2021FA.CSC.256.0001
# September 17th, 2021
# Programmers: Gabriel Henderson, Tiffany Harrell, Joshua Haley, Alan Gallardo

import pytest
import retirement


# boundary testing of the calculate function (very long function)
def test_calculate_nra_1938_january():
    assert retirement.calculate_nra(1938, 1) == ('65 and 2 months', 'March of 2003')


def test_calculate_nra_1938_november():
    assert retirement.calculate_nra(1938, 11) == ('65 and 2 months', 'January of 2004')


def test_calculate_nra_1955_january():
    assert retirement.calculate_nra(1955, 1) == ('66 and 2 months', 'March of 2021')


def test_calculate_nra_1955_november():
    assert retirement.calculate_nra(1955, 11) == ('66 and 2 months', 'January of 2022')


def test_calculate_nra_1939_january():
    assert retirement.calculate_nra(1939, 1) == ('65 and 4 months', 'May of 2004')


def test_calculate_nra_1939_november():
    assert retirement.calculate_nra(1939, 11) == ('65 and 4 months', 'March of 2005')


def test_calculate_nra_1956_january():
    assert retirement.calculate_nra(1956, 1) == ('66 and 4 months', 'May of 2022')


def test_calculate_nra_1956_november():
    assert retirement.calculate_nra(1956, 11) == ('66 and 4 months', 'March of 2023')


def test_calculate_nra_1940_january():
    assert retirement.calculate_nra(1940, 1) == ('65 and 6 months', 'July of 2005')


def test_calculate_nra_1940_november():
    assert retirement.calculate_nra(1940, 11) == ('65 and 6 months', 'May of 2006')


def test_calculate_nra_1957_january():
    assert retirement.calculate_nra(1957, 1) == ('66 and 6 months', 'July of 2023')


def test_calculate_nra_1957_november():
    assert retirement.calculate_nra(1957, 11) == ('66 and 6 months', 'May of 2024')


def test_calculate_nra_1941_january():
    assert retirement.calculate_nra(1941, 1) == ('65 and 8 months', 'September of 2006')


def test_calculate_nra_1941_november():
    assert retirement.calculate_nra(1941, 11) == ('65 and 8 months', 'July of 2007')


def test_calculate_nra_1958_january():
    assert retirement.calculate_nra(1958, 1) == ('66 and 8 months', 'September of 2024')


def test_calculate_nra_1958_november():
    assert retirement.calculate_nra(1958, 11) == ('66 and 8 months', 'July of 2025')


# def test_calculate_nra_1942_january():
# def test_calculate_nra_1942_november():
# def test_calculate_nra_1959_january():
# def test_calculate_nra_1959_november():
# def test_calculate_nra_1960_january():
# def test_calculate_nra_3000_january():
# def test_calculate_nra_1899_invalid_year():

# testing invalid inputs to calculate function
# def test_calculate_nra_string_input():
# def test_calculate_nra_negative_input():
