"""
1 = enemy
0 = no enemy

Puts the images into a spreadsheet for CustomDataset to use

"""
import os
import random
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def main(enemy_train_path, none_train_path, enemy_test_path, none_test_path, enemy_valid_path, none_valid_path):
    create_train_lists(enemy_train_path, none_train_path)
    create_test_lists(enemy_test_path, none_test_path)
    create_valid_lists(enemy_valid_path, none_valid_path)


def create_train_lists(enemy_path, none_path):
    e_col1 = []
    n_col1 = []
    e_col2 = []
    n_col2 = []
    for r, d, f in os.walk(enemy_path):
        for file in f:
            if '.png' in file:
                e_col1.append(file)
                e_col2.append(1)

    for r, d, f in os.walk(none_path):
        for file in f:
            if '.png' in file:
                n_col1.append(file)
                n_col2.append(0)

    random.shuffle(e_col1)
    random.shuffle(n_col1)
    create_train_excel(e_col1, n_col1, e_col2, n_col2)


def create_test_lists(enemy_path, none_path):
    e_col1 = []
    n_col1 = []
    e_col2 = []
    n_col2 = []
    for r, d, f in os.walk(enemy_path):
        for file in f:
            if '.png' in file:
                e_col1.append(file)
                e_col2.append(1)

    for r, d, f in os.walk(none_path):
        for file in f:
            if '.png' in file:
                n_col1.append(file)
                n_col2.append(0)

    random.shuffle(e_col1)
    random.shuffle(n_col1)
    create_test_excel(e_col1, n_col1, e_col2, n_col2)


def create_valid_lists(enemy_path, none_path):
    e_col1 = []
    n_col1 = []
    e_col2 = []
    n_col2 = []
    for r, d, f in os.walk(enemy_path):
        for file in f:
            if '.png' in file:
                e_col1.append(file)
                e_col2.append(1)

    for r, d, f in os.walk(none_path):
        for file in f:
            if '.png' in file:
                n_col1.append(file)
                n_col2.append(0)

    random.shuffle(e_col1)
    random.shuffle(n_col1)
    create_valid_excel(e_col1, n_col1, e_col2, n_col2)


def create_train_excel(e_col1, n_col1, e_col2, n_col2):
    e_col1.extend(n_col1)
    e_col2.extend(n_col2)
    train_df = pd.DataFrame({'path': e_col1, 'class': e_col2})
    train_df.to_excel('C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/training_data/train_set.xlsx',
                      header=False, index=False)


#  train_df.to_excel(os.getenv("TRAIN_SPREADSHEET"),
#                 header=False, index=False)


def create_test_excel(e_col1, n_col1, e_col2, n_col2):
    e_col1.extend(n_col1)
    e_col2.extend(n_col2)
    test_df = pd.DataFrame({'path': e_col1, 'class': e_col2})
    test_df.to_excel('C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/testing_data/test_set.xlsx',
                     header=False, index=False)


def create_valid_excel(e_col1, n_col1, e_col2, n_col2):
    e_col1.extend(n_col1)
    e_col2.extend(n_col2)
    train_df = pd.DataFrame({'path': e_col1, 'class': e_col2})
    train_df.to_excel('C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/valid_data/valid_set.xlsx',
                      header=False, index=False)

    # test_df.to_excel(os.getenv("TEST_SPREADSHEET"),
    #                 header=False, index=False)


if __name__ == '__main__':
    """main(enemy_train_path=os.getenv("ENEMY"),
         none_train_path=os.getenv("NONE"),
         enemy_test_path=os.getenv("RANENEMY"),
         none_test_path=os.getenv("RANNONE"),
         )"""
    main(enemy_train_path=r'C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/training_data/enemy',
         none_train_path=r'C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/training_data/none/',
         enemy_test_path=r'C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/testing_data/enemy',
         none_test_path=r'C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/testing_data/none',
         enemy_valid_path=r'C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/valid_data/enemy',
         none_valid_path=r'C:/Users/Luc/Documents/CPS 803/Main Project/src/pytorch/data/valid_data/none',
         )
