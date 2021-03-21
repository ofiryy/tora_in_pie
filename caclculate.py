import os
import json
# import yaml

regular_gimatryia = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "כ": 20,
    "ך": 20,
    "ל": 30,
    "מ": 40,
    "ם": 40,
    "נ": 50,
    "ן": 50,
    "ס": 60,
    "ע": 70,
    "פ": 80,
    "ף": 80,
    "צ": 90,
    "ץ": 90,
    "ק": 100,
    "ר": 200,
    "ש": 300,
    "ת": 400
}


small_gimatryia = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 1,
    "כ": 2,
    "ך": 2,
    "ל": 3,
    "מ": 4,
    "ם": 4,
    "נ": 5,
    "ן": 5,
    "ס": 6,
    "ע": 7,
    "פ": 8,
    "ף": 8,
    "צ": 9,
    "ץ": 9,
    "ק": 1,
    "ר": 2,
    "ש": 3,
    "ת": 4
}
def sum_of_pie_digits(number_of_digits_to_sum):
    pie = ""
    sum_of_digits = 0
    with open("./pie.txt") as pie_file:
        pie = pie_file.read().replace(" ", "")
    number_of_digits_to_sum_range = range(number_of_digits_to_sum)
    for digit in number_of_digits_to_sum_range:
        sum_of_digits += int(pie[digit])
    return sum_of_digits

def get_regular_gimatriya_value(hebrew_sentence):
    sum = 0
    for letter in hebrew_sentence.replace(" ", ""):
        sum += regular_gimatryia[letter]
    return sum

def get_small_gimatriya_value(hebrew_sentence):
    sum = 0
    for letter in hebrew_sentence.replace(" ", ""):
        sum += small_gimatryia[letter]
    return sum

if __name__ == "__main__":

    with open("psukim.txt", "r", encoding="utf8") as psukim_file:
        psukim = psukim_file.read().split("\n")
        tora = psukim[0]
        first_pasuk = psukim[1]
        tora_reg_gim = get_regular_gimatriya_value(tora)
        tora_small_gim = get_small_gimatriya_value(tora)
        first_pasuk_reg_gim = get_regular_gimatriya_value(first_pasuk)
        first_pasuk_small_gim = get_small_gimatriya_value(first_pasuk)

        print(f'Regular gimatrya value of: "{tora}" is {tora_reg_gim}')
        print(f'Regular gimatrya value of: "{first_pasuk}" is {first_pasuk_reg_gim}')
        print(f'The sum of the first {tora_reg_gim}'
              f' digits of Pie (after the point) is- {sum_of_pie_digits(tora_reg_gim)}')

        print(f'Small gimatrya value of: "{tora}" is {tora_small_gim}')
        print(f'Small gimatrya value of: "{first_pasuk}" is {first_pasuk_small_gim}')
        print(f'The sum of the first {tora_small_gim}'
              f' digits of Pie (after the point) is- {sum_of_pie_digits(tora_small_gim)}')

