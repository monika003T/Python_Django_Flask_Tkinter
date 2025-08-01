a = 31
t = type(a)  # class <int> 
print (t)

b = 31.2 
t = type(b)
print (t) # class <float>

c = "adarsh"
t = type(c)
print (t) # class <string>

d = "31.2"
t = type(d)
print (t) # it is a floating point no. but it is underscpre then it is a string

# with same code if we want e as a floating point no.
e = "31.2"
f = float(e) # e but the type should be float
t = type(f)
print (t) # class <float>

