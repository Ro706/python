import random
choice = str(input("enter your choice (x or o): "))
if choice == "x":
    computer_choice = "o"
else:
    computer_choice = "x"    
print('''
      1     |     2       |    3
 -----------|-------------|------------
      4     |     5       |    6   
 -----------|-------------|------------
      7     |     8       |    9
      ''')
a,b,c,d,e,f,g,h,i ='1','2','3','4','5','6','7','8','9'
list1 = [1,2,3,4,5,6,7,8,9]
def user():
    user = int(input(f"enter your choice {list1}:"))
    if user == 1:
        a = choice      
    elif user == 2:
        b = choice
    elif user == 3:
        c = choice
    elif user == 4:
        d = choice
    elif user == 5:
        e = choice
    elif user == 6:
        f = choice
    elif user == 7:
        g = choice
    elif user == 8:
        h = choice
    elif user == 9:
        i = choice 
    else:
        print("error")                                                       
    print(f'''
      {a}     |     {b}       |    {c}
   -----------|---------------|------------
      {d}     |     {e}       |    {f}   
   -----------|---------------|------------
      {g}     |     {h}       |    {i}
      ''')
    list1.remove(choice)
def computer():
    while True:
        computer = random.randint(1,10)
        if computer in list1 :
           if computer == 1:
               a = computer_choice     
           elif computer == 2:
               b = computer_choice
           elif computer == 3:
               c = computer_choice
           elif computer == 4:
               d = computer_choice
           elif computer == 5:
               e = computer_choice
           elif computer == 6:
               f = computer_choice
           elif computer == 7:
               g = computer_choice
           elif computer == 8:
               h = computer_choice
           elif computer == 9:
               i = computer_choice
           else:
               print("error")         
           print(f'''
                {a}     |     {b}       |    {c}
             -----------|---------------|------------
                {d}     |     {e}       |    {f}   
             -----------|---------------|------------
                {g}     |     {h}       |    {i}
               ''')
           list1.remove(computer_choice)
           break
        else:
            continue    
while len(list1) >= 0:
    if choice == "x":
        for i in range(0,9):
            user()
            computer()
    else:
        for i in range(0,9):
            computer()
            user()
print("thank you for playing this game")               
        



