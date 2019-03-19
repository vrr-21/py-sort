from heap_sort import heap_sort
import sys
import timeit

def load_file(f):
    file_reader = open(f, 'r')
    s = file_reader.readline()
    str_array = s.split()
    return list(map(int, str_array))

if __name__ == "__main__":
    print_nums = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "--print":
            print_nums = True
    ip_list = load_file("random_files/test-file1000000.txt")
    n = len(ip_list)
    print("Length of list: "+str(n))
    if print_nums:
        print("List before sorting: "+str(ip_list))
    start = timeit.default_timer()
    heap_sort(ip_list)
    stop = timeit.default_timer()
    if print_nums:
        print("List after sorting: "+str(ip_list))
    print("Runtime: "+str(stop - start))
