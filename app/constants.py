TRANSPILE_PROMPT = """Python --> JS
Transform the input python function to a javascript function

###
Input:
def sum_and_check_if_42(a, b):
    c = a + b
    if c == 42:
        return True
    else:
        return False

###
Output:
function sum_and_check_if_42(a, b) {
    var c = (a + b);
    if (c === 42) {
        return true
        } else {
            return false
            }
};

###
Input:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

###
Output:"""

EXPLAIN_WORD = """What does the word "link" mean in the following sentence?
Sentence: The excavation machine malfunctioned due to a broken link.
Meaning: a ring or loop in a chain.

What does the word "bank on" mean in the following sentence?
Sentence: I was banking on my team winning the next game as well.
Meaning: to depend on something.

What does the word "drop" mean in the following sentence?
Sentence: the drop in subscriptions in May was cause for alarm.
Meaning:"""

CATCHY_PROMPT = """Catchy screamer headline for a column about Elizabeth II small feet: "Queen size".
Catchy screamer headline for a column about a CEO who needs the board : "May the board be with you".
Catchy screamer headline for a column about leaving to Australia: "Down the kangaroo hole".
Catchy screamer headline for a column about golf balls: "The rubber the better".
Catchy screamer headline for a column about the clothing industry during the wedding season: "Changing groom".
Catchy screamer headline for a column about the changes council members were texting each other: "Texting while bored".
Catchy screamer headline for a column about European eggs pasteurization laws: "The egg on Europe's face".
Catchy screamer headline for a column about the royal family's new dog: "Let them eat cats".
Catchy screamer headline for a column about hazards of wearing skinny jeans: "Killer Tight".
Catchy screamer headline for a column about text messaging at funerals:"""