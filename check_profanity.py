import urllib.request

def read_text():
    quotes = open('movie_quotes.txt')
    text_to_check = quotes.read()
    quotes.close()
    # print(text)
    
    # need to filter out bad whitespace or it returns "HTTP Error 400: Bad Request"
    text_to_check = ''.join(text_to_check.split())
    # text_to_check = 'shit  '
    check_profanity(text_to_check)


def check_profanity(text_to_check):
    
    url_to_check = 'http://www.wdylike.appspot.com/?q=' + text_to_check
    connection = urllib.request.urlopen(url_to_check)
    output = str(connection.read())
    print(url_to_check)
    print(output)
    connection.close()
    if "true" in output:
        print('PROFANITY!')
    elif "false" in output:
        print('No profane words detected')
    else:
        print('Failed to detect a true or false.')
    print('\n')

read_text()

