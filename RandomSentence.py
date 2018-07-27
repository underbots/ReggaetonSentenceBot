from random import choice

def word_column(file_name): #Recibe un fichero y crea una lista donde cada elemento es una línea del fichero
    input_file = open(file_name)
    column = []
    for line in input_file:
        column.append(line.strip())
    input_file.close()
    return column

def word_table(file_list): #Recibe una lista de ficheros y los incorpora a una tabla
    table = []
    for file in file_list:
        table.append(word_column(file))
    return table


'''
Lista de archivos y obtención de datos
Lo hago aquí para que se cargue al comienzo del programa y evitar llamar continuamente a las funciones anteriores
'''
random_file_list = ['./data/a.txt', './data/b.txt', './data/c.txt', './data/d.txt', './data/e.txt', './data/f.txt']
random_data = word_table(random_file_list)


def random_sentence(subject = False):
    sentence = ""
    if subject:
        sentence += subject + " "
        start_word = 1 #ya se tiene el sujeto y la frase empieza en la segunda palabra
    else:
        start_word = 0
    for i in range(start_word, len(random_data)):
        sentence += choice(random_data[i]) + " "
    return sentence

def random_verse(subject = False):
    length_verse = 4
    verse = ""
    for i in range(0, length_verse):
        verse += random_sentence(subject) + '\n'
    return verse
