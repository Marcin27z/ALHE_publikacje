class FileLogger:

    def __init__(self, file_name: str):
        self.file = open(file_name, "a+")
        self.file.write("-" * 100 + "\n")
        self.k = 1

    def log_K(self, k):
        self.k = k
        self.file.write("K wynosi {}\n".format(k))
        self.file.flush()

    def log_max_list(self, max_list):
        for index, max_value in enumerate(max_list):
            self.file.write("Po {} wywolaniach najlepsza wartosc wynosi: {}\n".format(pow(10, index) * self.k, max_value))
        self.file.flush()

    def log_result(self, result):
        self.file.write(' '.join(map(str, result)) + "\n")
        self.file.flush()

    def log_start_point(self, start_point):
        self.file.write(str(start_point))
        self.file.write("\n")
        self.file.flush()

    def close(self):
        self.file.close()

    def __del__(self):
        self.close()


if __name__ == '__main__':
    fl = FileLogger("hello")
    fl.log_K(10)
    fl.log_max_list([23, 21, 33, 43])
    fl.close()
