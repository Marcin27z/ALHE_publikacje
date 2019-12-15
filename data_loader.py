from ast import literal_eval


# plik musi zawierać nową linię na końcu pliku
# zwróć słownik zawierający pary klucz-wartość z pliku
def load_data(file_name):
    with open(file_name, mode='r') as file:
        lines = file.readlines()
        lines = list(filter(lambda x: x != '\n', lines))
        lines = [line[:-2] for line in lines]
        parameters = {key: literal_eval(value) for key, value in [line.split(' = ') for line in lines]}
        return parameters

