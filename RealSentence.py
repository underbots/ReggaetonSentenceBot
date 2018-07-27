from random import choice

real_file_name = './data/real.txt'
input_real_file = open(real_file_name)
real_data = input_real_file.readlines()
input_real_file.close()

def real_sentence():
    return choice(real_data)
