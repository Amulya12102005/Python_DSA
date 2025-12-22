# Hashmap={"name":"Raju",
# "rollno":1202,
# "year":"3rd year"}
# try:
#     print(Hashmap["salary"])
# except KeyError:
#     print("check")

# a=24
# b="26"
# try:
#     result=a/b
# except TypeError:
#     print("check your datatype")
# else:
#     print(result)

try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    result=a+b
except TypeError:
    print("check your datatype")
except ValueError:
    print("input must be a int datatype")
else:
    print(result)
finally:
    print("end of the code")
