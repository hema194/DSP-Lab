str1="hema"
str2="KANAKA MAHA LAKSHMI"
str3="hema194a"
str4="7286023194"
str5=" "
str6="Amma Nanna"
str7="Welcome to my world"
s1="abc"
s2="123"
s3="hema,kanaka,maha,lakshmi"
#String CONCATENATION:
print("CONCATenation of str1 and str2 : ",str1+str2)
#String REPETITION:
print("str1 repetition : ",str1*2)
#string slice:
print("slice :",str1[1])
#string range:
print("range :",str1[0:])
#string range slice:
print("range slice : ",str2[0:19])
print("nrange slice : ",str1[1:3])
#membership[in]:
print("membership in : ",'e' in str1)
print("membership in : ",'f' in str1)
#membership[not in]:
print("membership not in : ",'a' not in str1)

#STRING FUNCTIONS ::
#string capitalize():
print("\ncapitalize :",str1.capitalize())
print("\ncapitalize :",str7.capitalize())
#string count():
print("count :",str2.count("A"))
#string lower():
print("lower :",str2.lower())
#string upper():
print("upper :",str1.upper())
#string isalpha():
print("isalpha :",str1.isalpha())
#string isdigit():
print("isdigit :",str4.isdigit())
#islower():
print("islower :",str1.islower())
#isupper():
print("isupper :",str1.isupper())
#isspace():
print("isspace :",str2.isspace())
print("isspace :",str5.isspace())
#istitle():
print("istitle :",str2.istitle())
print("istitle :",str6.istitle())
#partition():
print("partition :",str7.partition("to"))
#join():
print("join s1 and s2 :",s1.join(s2))
print("join s1 and s2 :",s2.join(s1))
#replace():
print("replace :",str2.replace("MAHA","gold"))
#split():
print("split :",str2.split())
print("split :",s3.split(","))
print("split :",s3.split(":"))#waste
#swapcase:
print("swapcase :",str6.swapcase())
#length:
print("length :",len(str1))
print("length :",len(str2))
#max:
print("max :",max(str1))
print("max :",max(str4))
#min:
print("min :",min(str1))
print("min :",min(str4))
#isalnum()
print("isalphanum:",str3.isalnum())
d={1:"a",2:"b",3:"c"}
print(d)
print(d)
print(d)
print(d)
#index()
a="Data Science"
print(a.index("t"))
#find()
print(a.find("S"))
