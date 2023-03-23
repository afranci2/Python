#!/usr/bin/env python
# coding: utf-8

# In[1]:


# function name: q1
# argument(s): none
# description: assign points based on class year
# return: return the point total for the first question
def q1():
    print("QUESTION 1")

    # Keeps track of the point total for the first question
    score = 0

    # Ask the user what class year they are
    year_ans = input("What year are you? (1, 2, 3, 4): ")

    # Current Freshman = 1 point
    if year_ans == "1":
        score += 1

    # Current Sophomore = 2 points
    elif year_ans == "2":
        score += 2

    # Current Junior = 3 points
    elif year_ans == "3":
        score += 3

    # Current Senior = 4 points
    elif year_ans == "4":
        # Ask the user if they are about to graduate
        #     ONLY a 4th year student would receive this question
        graduate = input("Are you about to graduate? (y = yes, n = no): ")

        # If they say yes, they receive no points.
        if graduate.lower() == 'n' or graduate.lower() == 'no':
            score += 4

    # Ask the user how old they are
    years_old = input("How old are you?: ")

    # If the student is >= 23 years old, give them another point
    if int(years_old) >= 23:
        score += 1

    # Return the point total for the first question
    return score


# function name: q2
# argument(s): none
# description: assign points based on if full-time student
# return: return the point total for the second question
def q2():
    # Assign points based on if full-time student
    print("\nQUESTION 2")

    # Keeps track of the point total for the second question
    score = 0

    # Ask the user if they are a full-time student
    full_time = input("Are you a full-time student? (y = yes, n = no): ")

    # If the student is full-time, give them another point
    if full_time.lower() == 'y' or full_time.lower() == 'yes':
        score += 1

    # Return the point total for the second question
    return score


# function name: q3
# argument(s): none
# description: assign points based on academic probation
# return: return the point total for the third question
def q3():
    # Assign points based on academic probation
    print("\nQUESTION 3")

    # Keeps track of the point total for the third question
    score = 0

    # Ask the user if they are currently on academic probation
    probation = input(
        "Are you currently on academic probation? (y = yes, n = no): ")

    # If the student is currently on academic probation, deduct a point
    if probation.lower() == 'y' or probation.lower() == 'yes':
        score -= 1

    # Return the point total for the third question
    return score


# function name: q4
# argument(s): none
# description: assign points based on possible academic suspension
# return: return the point total for the fourth question
def q4():
    # Assign points based on possible academic suspension
    print("\nQUESTION 4")

    # Keeps track of the point total for the fourth question
    score = 0

    # Ask the user if they are currently on academic suspension
    suspension = input(
        "Are you currently on a possible academic suspension? (y = yes, n = no): ")

    # If the student is currently on academic suspension, deduct 2 points
    if suspension.lower() == 'y' or suspension.lower() == 'yes':
        score -= 2

    # Return the point total for the fourth question
    return score


# function name: q5
# argument(s): none
# description: assign points based on disciplinary probation at any point during the academic year
# return: return the point total for the fifth question
def q5():
    # Assign points based on disciplinary probation at any point during the academic year
    print("\nQUESTION 5")

    # Keeps track of the point total for the fifth question
    score = 0

    # Ask the user if they have been on disciplinary probation at any point during the academic year
    any_probation = input(
        "Have you been on a disciplinary probation at any point during the academic year? (y = yes, n = no): ")

    # If the student is currently on disciplinary probation at any point during the academic year, deduct 3 points
    if any_probation.lower() == 'y' or any_probation.lower() == 'yes':
        score -= 3

    # Return the point total for the fifth question
    return score


# function name: main
# argument(s): none
# description: sets up the program and manages functions calls for questions
# return: none
def main():
    # Keeps track of the point total during questions
    total = 0

    # A header to start the program
    print("-------------------------------")
    print("   HOUSING SCORE CALCULATOR")
    print("-------------------------------")
    print()

    # CALL each function AND store its RETURN value representing the point total for each question
    q1_score = q1()
    q2_score = q2()
    q3_score = q3()
    q4_score = q4()
    q5_score = q5()

    # Use the RETURN values (i.e., variables created on lines 151 to 155) to compute the total score
    total = q1_score + q2_score + q3_score + q4_score + q5_score

    # At the end of the program, tell the user their score
    print()
    print("------YOUR HOUSING SCORE----------")
    print("Your housing points score is", total)
    print("----------------------------------")


# Call the main function to run the program
main()


# In[ ]:
