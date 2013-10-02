#Method 1: Its just too simple
x = "apple"
y = (" "* 20)
c = x+y
print ("Method 1:"+c)

#Method 2: LJust Methods
a = 'apple'
print("Method 2:"+a.ljust(20))

#Method 3: Expand tabs
b = 'apple\t'
print("Method 3:"+b.expandtabs(20))
print "%-20s" %a
