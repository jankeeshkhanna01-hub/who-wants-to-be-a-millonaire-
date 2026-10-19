li = [["1. Which planet is known as the Red Planet?","A. Venus","B. Mars","C. Jupiter", "D. Saturn" , "b"],
       ["2.What is the brain of a computer called?","A. ram","B. hard disk","C. cpu", "D. monitor","c"],
       ["3. What is the capital of Australia?","A. sydney","B. Mellbourne","C. canverra", "D. perth","c"],
       ["4. What is 15 × 4?","A. 45","B. 60","C. 75", "D. 90","b"],
       ["5. Which language is primarily used to structure web pages?","A. html","B. python","C. Java", "D. c","a"],
       ["6. How many sides does a hexagon have?","A.  5","B.6","C. 7", "D. 8","b"],
       ["7. Who wrote the play Romeo and Juliet?","A. charles","B. william","C. Jupiter", "D. Sagdwyd","b"],
       ["8. Which gas do plants absorb during photosynthesis?","A. oxygen","B. nitrogen","C. carbon", "D. hydrogen","c"],
       ["9. What does CSS stand for in web development?","A. cascading style sheets","B. Mars","C. Jupiter", "D. Saturn","a"],
       ["10. Which data structure follows the LIFO principle?","A. stack","B. queue","C. Jupiter", "D. Saturn","a"],
      ]
for questions in li:
    print(questions[0])
    print( f"a. {questions[1]}")
    print( f"b. {questions[2]}")
    print( f"c. {questions[3]}")
    print( f"d. {questions[4]}")
    a=input("enter your answer:")
    if (a==questions[5]):
        print("correct")
    else:
        print("wrong  ... better luck next time!!")
        break
 