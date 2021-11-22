# -- FILE: retirement.py
  Feature: Calculate Retirement
    Rule: Birthdate must be a valid date after 1/1/1900
      Scenario: Calculates Retirement
        Given An Input date
        And The date is valid
        When I calculate the retirement date
        Then I should return the date for retirement
      Scenario: Invalid Date
        Given An input date
        But The Date is invalid
        Then I should return an error message saying unable to calculate retirement
