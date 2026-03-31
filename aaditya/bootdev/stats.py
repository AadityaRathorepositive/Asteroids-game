
store={}

def get_book_text(get_book_path):
    with open(get_book_path) as main:
        file_content= main.read()
        def count_word():
            splitted_words=file_content.split()
            i=0
            for splitted_words[i] in splitted_words:
                i+=1
            return i
        return_i=count_word()
        count_of_each_word(file_content)
    return return_i



def count_of_each_word(file_content):
    file_content_in_lower=file_content.lower().split()
    for word in file_content_in_lower:
        for letter in word:
            if letter.isalpha() and letter not in store:
                store[letter]=1    
            elif letter in store:
                store[letter]=store[letter]+1


#count_char=get_book_text()


#print(sorted_list)
