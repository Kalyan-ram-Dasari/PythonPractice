questions = [
    {
    'q' : "What is the output of bool([])?",
    'options': ["A) True", "B) False", "C) []", "D) None"],
    'answer' : 'B'
    },
    {
       "q": "Which method adds an element at the end of a list?",
        "options": ["A) insert()", "B) append()", "C) extend()", "D) push()"],
        "answer": "B"
    },
    {
        "q": "What is the output of 3 * 'ab'?",
        "options": ["A) ababab", "B) ab3", "C) ab ab ab", "D) Error"],
        "answer": "A"
    },
    {
        "q": "Which data type is returned by input() in Python 3?",
        "options": ["A) str", "B) int", "C) float", "D) bool"],
        "answer": "A"
    },
    {
        "q": "What does len({'a':1, 'b':2}) return?",
        "options": ["A) 2", "B) 1", "C) 3", "D) Error"],
        "answer": "A"
    },
    {
        "q": "Which operator is used for floor division?",
        "options": ["A) /", "B) //", "C) %", "D) **"],
        "answer": "B"
    },
    {
        "q": "What is the output of set('hello')?",
        "options": ["A) {'h','e','l','o'}", "B) ['h','e','l','o']", "C) {'hello'}", "D) Error"],
        "answer": "A"
    },
    {
        "q": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C"
    },
    {
        "q": "What is the output of 5 == 5.0?",
        "options": ["A) True", "B) False", "C) Error", "D) None"],
        "answer": "A"
    },
    {
        "q": "Which module is used for working with regular expressions?",
        "options": ["A) regex", "B) re", "C) regexp", "D) match"],
        "answer": "B"
    }
]

score = 0
for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['q']}")
    for opt in q['options']:
        print(opt)
    user_ans = input("Your answer (A/B/C/D): ").strip().upper()
    
    if user_ans == q['answer']:
        print("correct answer")
        score+=1
    else:
        print(f"Wrong! Correct answer is {q['answer']}") 
        
print("\n--- Quiz Completed ---")
print(f"Your Score: {score}/10")

if score == 10:
    print("Excellent! You got 10/10")
elif score >= 6:
    print("Average performance")
elif score >= 4:
    print("Needs improvement")
else:
    print("Fail — Keep practicing!")            
        