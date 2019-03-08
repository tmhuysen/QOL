"""
Transform a list of elements to a comma separated line
    eg. [1, 2, 3, 4] becomes:
        1,2,3,4
"""


def array_to_csl(array):
    s = ''.join([str(el) + "," for el in array])
    return s[:-1]


"""
Transform a string into an tuple of n+1 lists of m elements 
 (where n = amount of tabs per newline, and m = amount of new lines)

@param string               string containing all data (eg. an entire file read to a string)
@param define_type          if given, transforms the read elements into given type

@return tuple of data sets
"""


def newlined_tabbed_data_string_to_dataset(string, define_type = None):

    string_list = string.strip("\n").split("\n")
    index = 0
    is_start_correct = True
    if define_type is not None:
        while is_start_correct:
            try:
                x = string_list[index].split("\t")
                for t in x:
                    define_type(t)
                is_start_correct = False
            except ValueError:
                index += 1
    line_length = len(string_list[index].split("\t"))
    total_set = list()
    for i in range(line_length):
        total_set.append(list())
    for j in range(index, len(string_list)):
        line = string_list[j]
        split_line = line.strip("\n").split("\t")

        for i in range(line_length):
            if define_type is None:
                total_set[i].append(split_line[i])
            else:

                total_set[i].append(define_type(split_line[i]))
    return tuple(total_set)
