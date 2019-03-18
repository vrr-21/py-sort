from bubble_sort import bubble_sort
import sys
import timeit

def load_file(f):
    file_reader = open(f, 'r')
    s = file_reader.readline()
    str_array = s.split()
    return list(map(int, str_array))

if __name__ == "__main__":
    ip_list = load_file("test-file10.txt")
    print("List before sorting: "+str(ip_list))
    start = timeit.default_timer()
    bubble_sort(ip_list)
    stop = timeit.default_timer()
    print("List after sorting: "+str(ip_list))
    print("Runtime: "+str(stop - start))
