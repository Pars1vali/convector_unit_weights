import pandas as pd

def distribution_unit(unit_name, value):
    df = None
    match unit_name:
        case 'kg':
            df = convert_weight_kg(value)
        case 'gr':
            df = convert_weight_grams(value)
        case 'lb':
            df = convert_weight_pounds(value)
        case 'oz':
            df = convert_weight_ounces(value)
    return df
def convert_weight_kg(weight_in_kg):
    # Конвертация в граммы
    weight_grams = weight_in_kg * 1000

    # Конвертация в унции
    weight_ounces = weight_in_kg * 35.274

    # Конвертация в фунты
    weight_pounds = weight_in_kg * 2.205

    df = pd.DataFrame({'Единица измерения': ['Граммы', 'Унции', 'Фунты'],
                       'Значение': [weight_grams, weight_ounces, weight_pounds]})
    return df
def convert_weight_grams(weight_in_grams):
    # Перевод из грамм в килограммы
    weight_in_kg = weight_in_grams / 1000.0

    # Перевод из грамм в унции (1 грамм = 0.03527396 унции)
    weight_in_ounces = weight_in_grams * 0.03527396

    # Перевод из грамм в фунты (1 грамм = 0.00220462 фунта)
    weight_in_pounds = weight_in_grams * 0.00220462

    df = pd.DataFrame({'Единица измерения': ['Килограммы', 'Унции', 'Фунты'],
                       'Значение': [weight_in_kg, weight_in_ounces, weight_in_pounds]})
    return df
def convert_weight_ounces(weight_in_ounces):
    # Перевод из унций в килограммы
    weight_in_kg = weight_in_ounces * 0.0283495

    # Перевод   из унций   из граммы
    weight_in_grams = weight_in_ounces * 28.3495

    # Перевод из унций в фунты
    weight_in_pounds = weight_in_ounces * 0.0625

    df = pd.DataFrame({'Единица измерения': ['Килограммы', 'Граммы', 'Фунты'],
                       'Значение': [weight_in_kg, weight_in_grams, weight_in_pounds]})
    return df
def convert_weight_pounds(weight_in_pounds):
    # Перевод из унций в килограммы
    weight_in_kg = weight_in_pounds * 0.453592

    # Перевод  из унций   из граммы
    weight_in_grams = weight_in_pounds * 453.592

    # Перевод из унций в фунты
    weight_in_ounces = weight_in_pounds * 16

    df = pd.DataFrame({'Единица измерения': ['Килограммы', 'Граммы', 'Унции'],
                       'Значение': [weight_in_kg, weight_in_grams, weight_in_ounces]})
    return df
