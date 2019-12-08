from ast import literal_eval


# file needs to contain new line at the end of the file
# return dictionary containing key value pairs from file
def load_data(file_name):
    with open(file_name, mode='r') as file:
        lines = file.readlines()
        lines = list(filter(lambda x: x != '\n', lines))
        lines = [line[:-2] for line in lines]
        parameters = {key: literal_eval(value) for key, value in [line.split(' = ') for line in lines]}
        return parameters


if __name__ == '__main__':
    print(load_data("filozofia-input.txt"))
