# 4. WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found.
# def check_in_line():
#     word = "learning"
#     line_var = 0

#     with open("practice.txt", "r") as f:
#         while True:
#             content = f.readline()
#             if content == "":      # EOF reached
#                 break

#             line_var += 1
#             if word in content:
#                 print(f'Found "{word}" at line {line_var}')
#                 return

#     print(-1)

# def check_in_line():
#     word = "learning"

#     with open("practice.txt", "r") as f:
#         for line_no, line in enumerate(f, start=1):
#             if word in line:
#                 print(f'Found "{word}" at line {line_no}')
#                 return

#     print(-1)


def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()

# HA HA HA HA HA ......... HA
# You will never forget this question no. 4
# What a waste of time it was (1 hour seriously?)
# You were trying to debug why your code didn't work - where was the leak 
# tried copilot chatgpt - but at the end 
# you realized that you were defining the function and never called it (HA HA HA ...)
# AND you expect the program to run (HA HA HA ...)
# at the end you succed at the end wasting 1 hour.