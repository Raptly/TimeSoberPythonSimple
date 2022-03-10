import datetime


def display_time_sober():
    def calc_and_display_time_sober(rNum):
        calc_dates = (datetime.datetime.now() - datetime.datetime(2012, 4, 16)).days
        days_sober: int = calc_dates - rNum  # Number of total days sober
        years_sober = days_sober / 365  # Number of years sober
        result_days = print('You have', days_sober, 'days sober and')
        result_years = print(years_sober, 'years sober. Congrats!')
        return [result_days, result_years]


    calc_and_display_time_sober(4)


display_time_sober()
