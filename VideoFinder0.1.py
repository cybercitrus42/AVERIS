# YouTube URL search test
Search = input("What word would you like to learn? ")
SignSearch = (Search + "+asl+dictionary")
URL = f'https://youtube.com/results?search_query={SignSearch}'

print(URL)
