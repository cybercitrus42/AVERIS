# YouTube URL search test
Search = input("What word would you like to learn? ")
Search = Search.replace(" ","+")
signSearch = (Search + "+asl+dictionary")
URL = f'https://youtube.com/results?search_query={signSearch}'

print(URL)
