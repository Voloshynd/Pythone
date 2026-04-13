import sys
from file_utils import FileUtiles
from file_service import Processor


# python advanced_reader.py in.json out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# python advanced_reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# python advanced_reader.py in.txt out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# python advanced_reader.py in.pkl out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0

def main() -> None:
    FileUtiles.check_arguments(sys.argv)

    path_file_in = sys.argv[1]
    path_file_out = sys.argv[2]
    changes = sys.argv[3:]

    FileUtiles.check_path(path_file_in, f"Plik '{path_file_in}' nie istnieje.")
    FileUtiles.check_path(path_file_out,
                          f"Plik '{path_file_out}' nie istnieje.")

    file_format = path_file_in.split(".")[-1]
    data = FileUtiles.get_handler(file_format, path_file_in)
    obj = Processor(data, changes)
    obj.apply_changes()
    obj.show()
    obj.save_csv(path_file_out)


if __name__ == "__main__":
    main()
