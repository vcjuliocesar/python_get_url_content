import app

def run():
    while True:
        
        url = input("Enter a url site => ")
        app.get_url_content(url)
        answer = input('Do you want to check another url site? (yes/no) => ').lower()
        
        if answer != 'yes':
            print('Bye')
            break
    
    
if __name__ == '__main__':
    run()