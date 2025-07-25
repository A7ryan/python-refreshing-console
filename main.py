# Print Python Console like Professional

# e.g. Started
#      Started.
#      Started..    
#      Started...

# But the dots should refresh in single line
# 

from time import sleep

def python_fun_console():
    p = "."
    for i in range(4):
        sleep(1)
        # if you don't add end="", it will refresh full line (blink words)

        # uncomment this to get an idea
        # print("\033c")
        print("\033c", end="")
        print("Ready to Launch",i*p)
        if(i==3):
            sleep(1)

    print("You are 🔥")
    sleep(1)

python_fun_console()
