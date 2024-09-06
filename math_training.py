import random
import time

# Define available operators
OPERATORS = {
    "addition": "+",
    "subtraction": "-",
    "multiplication": "*",
    "division": "/"
}

# Operand range and total problems
MIN_OPERAND_SIMPLE = 1
MAX_OPERAND_SIMPLE = 12
MIN_OPERAND_ADVANCED = 1
MAX_OPERAND_ADVANCED = 50
TOTAL_PROBLEMS = 10


def generate_problem(operator, difficulty):
    if difficulty == "simple":
        min_operand = MIN_OPERAND_SIMPLE
        max_operand = MAX_OPERAND_SIMPLE
    elif difficulty == "advanced":
        min_operand = MIN_OPERAND_ADVANCED
        max_operand = MAX_OPERAND_ADVANCED
    else:
        raise ValueError("Invalid difficulty level")

    left = round(random.uniform(min_operand, max_operand), 2)
    right = round(random.uniform(min_operand, max_operand), 2)
    op = OPERATORS[operator]

    # Avoid division by zero
    if op == "/":
        while right == 0:
            right = round(random.uniform(min_operand, max_operand), 2)

    expr = f"{left} {op} {right}"
    try:
        answer = eval(expr)
        if op == "/":
            answer = round(answer, 2)  # Round division results
    except ZeroDivisionError:
        answer = "undefined"

    return expr, answer


def main():
    # User selects the type of problems to practice
    print("Select the type of problems you want to practice:")
    for key in OPERATORS.keys():
        print(f"- {key}")
    selected_operator = input("Enter your choice: ").strip().lower()
    if selected_operator not in OPERATORS:
        print("Invalid choice. Exiting...")
        return

    # User selects the difficulty level
    print("Select the difficulty level:")
    print("- simple")
    print("- advanced")
    difficulty = input("Enter your choice: ").strip().lower()
    if difficulty not in ["simple", "advanced"]:
        print("Invalid choice. Exiting...")
        return

    wrong = 0
    input("Press Enter to start!")
    print("---------------------")

    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem(selected_operator, difficulty)
        while True:
            try:
                guess = float(input(f"Problem #{i + 1}: {expr} = "))
                if abs(guess - answer) < 0.01:
                    break
                else:
                    print("Incorrect, try again.")
                    wrong += 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                wrong += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    m = int(total_time // 60)
    s = int(total_time % 60)



    print("---------------------")
    print(f"Nice work! You finished in {m} minutes and {s} seconds with {wrong} wrong attempts.")


if __name__ == "__main__":
    main()
