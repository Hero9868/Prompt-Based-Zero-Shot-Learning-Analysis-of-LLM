from get_results import inference


PROMPT = """Python --> JS
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


if __name__ == '__main__':
    print(PROMPT + inference(PROMPT))