def replace(file_name,find_word,replace_with_word):
    """ This is a simple function to read the text file and replace specific content of the file. 
    The function needs three inputs args;
        arg1="text_file_name", arg2="find_word", arg3="replace_with_word" """
    with open(file_name, "r+") as f:
        newstring=""
        for word in f.read().split():
            if word == find_word:
                word = replace_with_word
            newstring+=word+" "
        f.seek(0)
        f.write(newstring)
        f.close()

"Usage:"
replace('example.txt','placement','screening')