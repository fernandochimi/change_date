# coding: utf-8
import re
from time import mktime, strptime,\
    gmtime, strftime


def change_date(date, op, value):
    error = "The format date is invalid. "\
        "Please enter data with 'dd-mm-yyyy hh:mm' or 'dd/mm/yyyy hh:mm'"
    error_february = "February have only 28 days"
    error_operator = "Operator must be + or - only"

    split_blank = " ".join(date.split())
    new_parse = [int(p) for p in re.split(r'[ ,/:-]', split_blank) if p]

    day = new_parse[0]
    month = new_parse[1]
    year = new_parse[2]
    hour = new_parse[3]
    minute = new_parse[4]

    if day not in range(32) or month not in range(13) \
            or year < 0 or hour not in range(24) or minute not in range(60):
        print error
    elif (month == 2 and day not in range(29)) \
            or year < 0 or hour not in range(24) or minute not in range(60):
        print error_february
    else:
        seconds_time = strptime("{0}/{1}/{2} {3}:{4}".format(
            day, month, year, hour, minute), "%d/%m/%Y %H:%M")
        transform = mktime(seconds_time)

        if op == "+":
            add_min = transform + (int(value) * 60)
            print strftime("%d/%m/%Y %H:%M", gmtime(add_min))
        elif op == "-":
            sub_min = transform - (int(value) * 60)
            print strftime("%d/%m/%Y %H:%M", gmtime(sub_min))
        else:
            print error_operator

if __name__ == '__main__':
    date = raw_input("Enter with date: ")
    op = raw_input("Enter with a operator: ")
    value = raw_input("Enter with a value: ")
    change_date(date, op, value)
