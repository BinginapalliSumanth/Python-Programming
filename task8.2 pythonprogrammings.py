def my_generator(n):
     value = 0
     while value < n:
           yield value
           value += 1
for value in my_generator(3):
    print(value)
    
                 
