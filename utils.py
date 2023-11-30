def add_years_to_date(original_date, years_to_added):
    result = original_date.replace(original_date.year + years_to_added)
    return result


def check_number_presence_array(array, number):
    return number in array


def check_sum_of_array_to_number(array, number):
    return sum(array) >= number


