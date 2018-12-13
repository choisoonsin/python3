def ask_ok(prompt , retries=5 , reminder="Please try again!"):
    while True :
        ok = input(prompt)
        if ok in ('y' , 'yes') :
            return True
        
        if ok in ('n' , 'no') :
            return False
        
        retries = retries -1
        
        if retries < 0:
            raise ValueError('Invalid User response')
        print(reminder)
            
ask_ok('Please Insert your answer' , 2 , "Yes or No")
