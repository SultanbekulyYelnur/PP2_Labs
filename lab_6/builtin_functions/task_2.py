text = "Hello World"

upper = sum(map(str.isupper, text)) 
lower = sum(map(str.islower, text))  

print("Uppercase:", upper)  
print("Lowercase:", lower)  
