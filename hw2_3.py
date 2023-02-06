highest=0
for i in range(1,8):
    bug = int(input("How many bugs did you collect on day {}: ".format(i)))
    if bug>highest:
        highest=bug
print("The highest number of bugs collected this week is ", highest)