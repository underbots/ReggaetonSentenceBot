from random import choice

cunado_file_name = './data/cunado.txt'
input_cunado_file = open(cunado_file_name)
cunado_data = input_cunado_file.readlines()
input_cunado_file.close()

def cunado_sentence(subject = False):
    sentence = ""
    if subject:
        sentence += subject + ", "
    sentence += choice(cunado_data)
    return sentence
