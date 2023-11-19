try:
    print(x)
except:
    print("There was an error" )
except Exception as error:
    
finally:
    print("Im going to print with or without error")