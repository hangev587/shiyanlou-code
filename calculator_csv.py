#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import json

def read_csv(csv_path):
    csv_file = open(csv_path)
    usr_csv = csv.reader(csv_file)
    usr_list = list(usr_csv)
    csv_file.close()
    return usr_list


def calculator(income):
    start_point = 5000  # 起征点
    social_insurance_point = 0.08 + 0.02 + 0.005 + 0.06  # 社保比例
    # 需要缴税的那部分工资
    tax_part = income * (1 - social_insurance_point) - start_point
    if tax_part <= 0:
        tax = 0
    elif tax_part <= 3000:
        tax = tax_part * 0.03
    elif tax_part <= 12000:
        tax = tax_part * 0.1 - 210
    elif tax_part <= 25000:
        tax = tax_part * 0.2 - 1410
    elif tax_part <= 35000:
        tax = tax_part * 0.25 - 2660
    elif tax_part <= 55000:
        tax = tax_part * 0.3 - 4410
    elif tax_part <= 80000:
        tax = tax_part * 0.35 - 7160
    else:
        tax = tax_part * 0.45 - 15160
    salary = income * (1 - social_insurance_point) - tax
    return '{:.2f}'.format(salary)


def write_json(json_path, usr_dict):
    json_str = json.dumps(usr_dict)
    json_file = open(json_path, 'w')
    json_file.write(json_str)
    json_file.flush()
    json_file.close()
    pass


def main():
    csv_path = sys.argv[1]
    json_path = sys.argv[2]
    usr_list = read_csv(csv_path)
    usr_dict = {}
    for usr in usr_list:
        id, income = usr[0], float(usr[1])
        income = calculator(income)
        usr_dict[id] = income
        pass
    write_json(json_path, usr_dict)


if __name__ == "__main__":
    main()

