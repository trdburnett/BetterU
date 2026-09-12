import os, pickle

#saves a list to the given lists filepath
def save_list(file_path: str, savelist: list):
    if not os.path.exists(file_path):
        os.makedirs('data', exist_ok=True)
        f = open(file_path, 'x')
        f.close()
    with open(file_path, 'wb') as outp:
        pickle.dump(len(savelist), outp, pickle.HIGHEST_PROTOCOL)
        for item in savelist:
            pickle.dump(item, outp)