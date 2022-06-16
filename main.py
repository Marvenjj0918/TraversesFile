import csv
from csv import writer
import pandas
import pandas as pd
import zipfile
from zipfile import ZipFile
import os


# def read_file_CSV():
#     with open('Asia Prod 1.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             print(f'\t{row[0]} , {row[1]} , {row[2]}.')
#             line_count += 1


def zipfile_list():

    z = zipfile.ZipFile("zipfile.zip", "r")

    for filename in z.namelist():
        print ('File:', filename)
        z.namelist()
        df = pd.read_csv(z.open(filename))
        print(df)
        with open('countries.csv', 'a+', encoding='UTF8', newline='') as f:
            csv_writer = writer(f)

            # write the header
            csv_writer.writerow(df)

    # open zipped dataset
    #  with ZipFile('zipfile.zip', 'r') as zip:
    #     zip.printdir()

        # # open the csv file in the dataset
        #  with zip.open('Asia Prod 1.csv') as f:
        #      #read the dataset
        #      prod1 = pd.read_csv(f)
        #
        # with z.open("Asia Prod 2.csv") as f:
        #     # read the dataset
        #     prod2 = pd.read_csv(f)
        #
        #     # display dataset
        #     print(prod1.head())
            #print(prod1.head())
        #     prod1.to_csv('new_modify.csv')
        #     prod2.to_csv('new_modify.csv')


   # zf= zipfile.ZipFile('C:/Users/mjeanjac4/PycharmProjects/TraversesFile/zipfile.zip')
   # zf.namelist()
   # print(zf)
   # # df = pd.read_csv(zf.open('Asia Prod 1.csv'))
   # print(df)
        # Get list of files names in zip
        # listOfiles = zipObj.namelist()
        # Iterate over the list of file names in given list & print them
        #for elem in listOfiles:
            #ext = os.path.splitext(elem)[-1]  # Get extension of elem
            #if elem.filename.endswith('Bezirke.csv'):
              #  df = pd.read_csv(zip_file.open(elem.filename),
                                # delimiter=';',
                                 # header=0,
                                 # index_col=['Timestamp'],
                                 # parse_dates=['Timestamp']
                                 # )
                #df = pandas.read_csv('Zipfile/Asia Prod 1.csv')
           #      print(in_bytes)
           # # in_bytes.to_csv('new_modify.csv')
           #  print(elem)

# def read_file_pandas():
#     df = pandas.read_csv('Asia Prod 1.csv')
#     print(df)
#     df.to_csv('new_modify.csv')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read_file_CSV()
    #read_file_pandas()
    zipfile_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
