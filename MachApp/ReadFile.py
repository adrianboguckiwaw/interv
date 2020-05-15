import csv
from typing import Any, Tuple, Generator


class OpenFile(object):
    def OpenFiles(self,file):
        print("dickt!")
        result =[ ]
        with open(file, 'r') as file1:
            csv_file = csv.DictReader(file1)
            for row in csv_file:
                print(dict(row))
                result.append(dict(row))
        return result


class Run:
    of = OpenFile
    x =of.OpenFiles(of,'data.csv')
    print(x)

class MultipleVals:
    def MultipleIt(self,data_dict, currencies_dict, matching_dict):
        lists = []
        #for matching_id in data_dict:





