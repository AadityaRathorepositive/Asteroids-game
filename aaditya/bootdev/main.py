import sys
from stats import get_book_text,store

if len(sys.argv) != 2:
    print(f'Usage: python3 {sys.argv[0]} <path_to_book>')
    sys.exit(1)
else:
    dynamic_book_path=sys.argv[1]
    count_char=get_book_text(dynamic_book_path)

store_list=store.items()
def get_the_number(list_iteam):
    return list_iteam[1]

sorted_list=sorted(store_list,key=get_the_number,reverse=True)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {dynamic_book_path}")
print("----------- Word Count ----------")
print(f"Found {count_char} total words") 
print("--------- Character Count -------")
for character,count in sorted_list:
    print(f'{character}: {count}')
print("============= END ===============")

