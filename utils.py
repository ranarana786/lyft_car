def add_years_to_date(original_date, years_to_added):
    result = original_date.replace(original_date.year + years_to_added)
    return result
