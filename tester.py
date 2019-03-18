from simple_sort import simple_sort
import sys
def load_file(f):
    file_reader = open(f, 'r')
    s = file_reader.readline()
    str_array = s.split()
    return list(map(int, str_array))

if __name__ == "__main__":
    ip_list = load_file("test-file10000.txt")
    print("List before sorting: "+str(ip_list))
    simple_sort(ip_list)
    print("List after sorting: "+str(ip_list))