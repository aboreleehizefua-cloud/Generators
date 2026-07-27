"""
import socket 
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.connect(("example.com", 80))
request = request = "GET / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: MyCustomClient/1.0 (Ehizefua)\r\nAccept: text/html\r\nX-Developer: Ehizefua\r\nConnection: close\r\n\r\n"
sock.sendall(request.encode())

response = b""
while True:
    chunk = sock.recv(4096)
    if not chunk:
        break
    response += chunk

print(response.decode())
sock.close()

"""

"""def get_num_list():
    num_list =[]
    for n in range(num):
         num_list.append(n *1)
         return num_list
    

    num = 100000000
    num_index = get_num_list(num)
    print(num_index)

def get_num_gen(num):
    for n in range(num):
        yield n * 1
num = 1000000000

num_gen = get_num_gen(num)
for n in num_gen:
    print(n)
print (next(num_gen))
print(next(num_gen))      

def countdown(n):
    while n>0 :
        yield n
        n -=1

gen2 =countdown(5)
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
"""
#def fibonacci():
    #"""infinte fibonacci sequence"""
  #  a,b = 0,1
   # while True:
    #    yield a
     #   a,b = a+b

#gen = fibonacci ()

#take only the first 10 numbers
#for _ in range():
 #   print(next(gen), end =' ')

    # output: 0 1 1 2 3 5 8 13 21 34
"""
    #list comprehension
Gee_list = (x + x for x in range(200))

#matrix nested generators
matrix = [[2,4,6,8], [1,3,5,7], [3,5,6,9,], [1,2,4,8]]
fist = (num for row in matrix for num in row)
print(list(fist))    

#iterables
"""
"""
import itertools
def count_up(start = 0):
    n = start 
    while True:
        yield n
        n += 1

Glad= list(itertools.islice(count_up() , 8))
print(Glad)

genA = (x for x in [1,2,3])
genB = (x for x in [3,4,5])

combined = list(itertools.chain(genA , genB))
print(combined)

#ADVANCED GENERATORS
def acc():
    total = 0
    while True:
        value = yield total
        if value is None: 
            break

        total += value

print (acc())
gen = acc()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(8))
"""
# injecting 
"""
def safe_processor():
    while True:
        try:
            value = yield
            print(f"processing {value}")
        except ValueError as e:
            print(f"caught error: {e} , continuing...")
gen = safe_processor()
next(gen)

gen.send("hello")
gen.throw(ValueError, "bad data")
gen.send("world")

# shutting down generator
def resource_generator():
    print("Opening resource...")
    try:
        while True:
            yield "data"
    finally:
        print("Closing resource...")
gen = resource_generator()
print(next(gen))
print(next(gen))
gen.close()

"""
#Real life cases
def read_large_file (filepath):
    with open (filepath , "r") as f:
        for line in f:
            yield line.strip()
for line in read_large_file("C:\\Users\\HP\\OneDrive\\Documents\\log.txt"):
    print(repr(line))
    
gen = read_large_file("C:\\Users\\HP\\OneDrive\\Documents\\log.txt")
print(next(gen))
print("...doing something else in between...")
print(next(gen))

#fill in the blank 
def search_large_file(filepath , keyword):
    with open(filepath, "r") as f:
        for line in f:
            clean_line = line.strip() 
            if keyword in clean_line:
                yield clean_line
for line in search_large_file("C:\\Users\\HP\\OneDrive\\Documents\\log.txt", "need"):  
    print (line)            

# --- CSV reader below ---
def read_large_csv(filepath):
    """Read a CSV file line by line without loading it all into memory"""
    with open(filepath, 'r') as f:
        header = next(f).strip().split(',')
        for line in f:
            values = line.strip().split(',')
            yield dict(zip(header, values))

for row in read_large_csv('C:\\Users\\HP\\OneDrive\\Documents\\huge_dataset.csv'):
    print(row)
