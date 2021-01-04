import sys
from datetime import date 
  
fs=open("todo.txt","a")
fs.close()

fs=open("done.txt","a")
fs.close()

# Returns the current local date 
today = date.today() 

arguments = sys.argv

if len(arguments)<2:
    print('Usage :-')
    print('$ ./todo add "todo item"  # Add a new todo')
    print('$ ./todo ls               # Show remaining todos')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')
elif arguments[1]=="add":
    fs = open("todo.txt","a")
    fs.write(arguments[2])
    fs.write("\n")
    fs.close()
elif arguments[1]=="ls":
    fs = open("todo.txt","r")
    ln = fs.readline()
    cnt=0
    arr=[]
    while (ln):
        arr.append(ln)
        ln=fs.readline()
        cnt+=1
    fs.close()
    while(cnt>0):
        print("["+str(cnt)+"] "+str(arr[cnt-1]),end="")
        cnt-=1
elif arguments[1]=="del":
    fs = open("todo.txt","r")
    ls = fs.read().split("\n")
    fs.close()
    ls.pop()
    if len(ls)<int(arguments[2]):
        print("Error: todo #"+str(arguments[2])+" does not exist. Nothing deleted.")
    else:    
        ls.pop(int(arguments[2])-1)

        fs = open("todo.txt","w")
        for x in ls:
            fs.write(x)
            fs.write("\n")
        fs.close()
        print("Deleted todo #"+str(arguments[2]))
elif arguments[1]=="done":
    fs = open("todo.txt","r")
    ls = fs.read().split("\n")
    fs.close()
    ls.pop()
    if len(ls)<int(arguments[2]):
        print("Error: todo #"+str(arguments[2])+" does not exist.")
    else:
        tmp = ls[int(arguments[2])-1]
        ls.pop(int(arguments[2])-1)
        fs = open("todo.txt","w")
        for x in ls:
            fs.write(x)
            fs.write("\n")
        fs.close()
        
        fs = open("done.txt","a")
        fs.write("x "+str(today)+" "+str(tmp))
        fs.write("\n")
        fs.close()
        print("Marked todo #"+str(arguments[2])+" as done.")
elif arguments[1]=="help":
    print('Usage :-')
    print('$ ./todo add "todo item"  # Add a new todo')
    print('$ ./todo ls               # Show remaining todos')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')
elif arguments[1]=="report":
    fs = open("todo.txt","r")
    td = fs.read().split("\n")
    fs.close()
    td.pop()

    fs = open("done.txt","r")
    dn = fs.read().split("\n")
    fs.close()
    dn.pop()
    print(str(today)+" Pending :",str(len(td))+" Completed :",str(len(dn)))
else:
    print('Usage :-')
    print('$ ./todo add "todo item"  # Add a new todo')
    print('$ ./todo ls               # Show remaining todos')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')