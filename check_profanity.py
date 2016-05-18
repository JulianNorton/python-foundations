import urllib.request

# easier see output delination
for i in range(1,5):
    print('')

def read_text():
    quotes = open('movie_quotes.txt')
    text_to_check = quotes.read()
    quotes.close()
    # print(text)
    
    # need to replace spaces or it returns "HTTP Error 400: Bad Request"
    text_to_check = text_to_check.replace(' ','+')

    text_to_check = 'shit  '
    check_profanity(text_to_check)


def check_profanity(text_to_check):
    
    url_to_check = 'http://www.wdylike.appspot.com/?q=' + text_to_check
    # print(url_to_check)
    connection = urllib.request.urlopen(url_to_check)
    # print(connection)
    output = connection.read()
    print(output)
    connection.close()

read_text()

