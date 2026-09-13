import os, pickle

#returns list of objects found at given filepath
def load_list(list_file_path:str)-> list:
    list_to_return = []
    if os.path.exists(list_file_path):
        with open(list_file_path, 'rb') as inp:
            #uses the first dump of the length of the list to know what to load from the file
            for _ in range(pickle.load(inp)):
                list_to_return.append(pickle.load(inp))
    return list_to_return