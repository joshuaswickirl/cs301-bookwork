import random
import string

# answer = "methinks it is like a weasel"
answer = "life is like a box of chocolates"

def infiniteMonkey(answer):

    length = len(answer)
    letters = string.ascii_letters[0:26] + " "

    # Initial string generation
    attempt = ""
    for index in range(length):
        char = random.choice(letters)
        attempt += char
    print(f"Initial attempt: {attempt}")

    no_answer = True
    if attempt == answer:
        no_answer = False

    answer_as_list = list(answer)
    attempt_as_list = list(attempt)
    num_of_attempts = 1
    while(no_answer):
        changes = False
        for i in range(length):
            if attempt_as_list[i] != answer_as_list[i]:
                # Generate random char and replace based on index
                random_char = random.choice(letters)
                attempt_as_list[i] = random_char
                changes = True
            else:
                pass
    
        if changes == False:
            break

        num_of_attempts += 1
        # Print attempts to watch for change
        print("".join(attempt_as_list))

    print(f"Number of attempts: {num_of_attempts}")

if __name__ == "__main__":
    infiniteMonkey(answer)