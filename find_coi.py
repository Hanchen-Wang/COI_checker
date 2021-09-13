import argparse
import re
from openpyxl import load_workbook

parser = argparse.ArgumentParser()
parser.add_argument('--file_name', type=str, default='./data/wei_wang.xml',
                    help='the name of the input file to find coi. Currently only support the xml file from dblp')
parser.add_argument('--years', type=str, default='2019,2020,2021',
                    help='the years need to check for COI.')
parser.add_argument('--pc_file', type=str, default='./data/pc_members.xlsx',
                    help='file with all pc members')


def check_conflict(first_name, last_name, coi_set):
    for coi_name in coi_set:
        if first_name in coi_name and last_name in coi_name:
            return True
    return False


args = parser.parse_args()
years = args.years.split(',')
coi_authors = set()
with open(args.file_name) as f:
    lines = f.readlines()
    num_lines = len(lines)
    i = 0
    while i < num_lines:
        current_line = lines[i]
        # print(current_line)
        if '<article key=' in current_line:
            temp_set = set()
            while '</article>' not in current_line:
                if '</author>' in current_line:
                    # print(re.split('<|>',current_line))
                    temp_set.add(re.split('<|>',current_line)[2])
                elif '<year>' in current_line:
                    paper_year = re.split('<|>',current_line)[2]
                    if paper_year in years:
                        coi_authors = coi_authors.union(temp_set)
                i+=1
                current_line = lines[i]
        i+=1

wb = load_workbook(filename = args.pc_file)
pc_sheet = wb['Sheet1']
for row in pc_sheet.values:
    name = row[0]+' '+row[1]
    if check_conflict(row[0], row[1], coi_authors):
        print(name)

