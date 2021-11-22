from datetime import datetime


retirement_info: dict = {
    **{x: (66, 0,  1) for x in range(1900, 1955)},
    1955: (66, 2,  2),
    1956: (66, 4,  3),
    1957: (66, 6,  4),
    1958: (66, 8,  5),
    1959: (66, 10, 6),
    **{x: (67, 0,  7) for x in range(1960, 2021)},
}


def time_until_full_retirement(dob: datetime) -> (int, int, datetime):
    (ret_age_year, ret_age_month, _) = retirement_info.get(dob.year)
    retirement_year: int = dob.year + ret_age_year
    if (dob.month + ret_age_month) > 12:
        return ret_age_year, ret_age_month, datetime(retirement_year + 1, (dob.month + ret_age_month) % 12, 1),
    return ret_age_year, ret_age_month, datetime(retirement_year, dob.month + ret_age_month, 1)


def calculate_retirement():
    dob_input: str = input("Enter in your birthday: MM/YYYY").strip()
    year, months, date = time_until_full_retirement(datetime.strptime(dob_input, "%m/%Y"))
    print("Your full retirement age is {} and {} months".format(year, months))
    print("This is in {:%B of %Y}".format(date))


if __name__ == "__main__":
    calculate_retirement()
