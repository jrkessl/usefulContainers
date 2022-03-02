import os

myVar = os.getenv("var1", "not found") # retrieves 'var1' environment variable. Defaults to 'not found' if not found. 
print("variableSpitter")
print("found value for var1: " + str(myVar))
print("goodbye.")
