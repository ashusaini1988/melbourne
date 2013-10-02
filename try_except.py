file_name = "test.csv"
default_file = "rodents.csv"

try:
    file = open(file_name)
except IOError:
    file = open(default_file)
    
except:
    print 'There was some other error'
    raise
    
print file.readline()
