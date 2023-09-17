def arithmetic_arranger(problems, solutions=False):
  if (len(problems) > 5):  # Check if there are too many problems
    return "Error: Too many problems."

  operators = list()  # Operator of each problem
  operator_pos = list()  # Index of operator within each problem
  sub_problems = list()  # Divided problems, clean operators and operands
  problem_sizes = list()  # Number of spaces for each problem

  # Check for valid operators
  for i in problems:
    for char_index, char in enumerate(i):
      if char == "+" or char == "-":
        operators.append(char)
        operator_pos.append(char_index)
        break

  # Check if operators in every problem
  if len(operator_pos) != len(problems):
    return "Error: Operator must be '+' or '-'."

  # Divide string into three parts: operand, operator, operand
  for index, item in enumerate(problems):
    first_operand = item[:operator_pos[index]]
    second_operand = item[operator_pos[index] + 1:]
    operator = operators[index]
    solution = 0

    # Parse operands to integers
    try:
      first_operand = int(first_operand)
    except ValueError:
      return "Error: Numbers must only contain digits."
    try:
      second_operand = int(second_operand)
    except ValueError:
      return "Error: Numbers must only contain digits."

    # Check for number of digits
    if first_operand > 9999 or second_operand > 9999:
      return "Error: Numbers cannot be more than four digits."

    # Save number of spaces a problem will occupy upon print
    problem_sizes.append(get_problem_size(first_operand, second_operand) + 2)

    # Get solution to problem if requested in fun call
    if solutions is True:
      if (operator == "+"):
        solution = first_operand + second_operand
      else:
        solution = first_operand - second_operand
      sub_problem = [first_operand, second_operand, operator, solution]
    else:
      sub_problem = [first_operand, second_operand, operator]

    sub_problems.append(sub_problem)  # Add clean problem to list

  # Variables for formatting
  problem_space = "    "  # Fixed space between problems
  f_line = ""  # First line
  s_line = ""  # Second line
  d_line = ""  # Dash line
  sol_line = ""  # Solutions line

  # Format first line
  for index, item in enumerate(sub_problems):
    operand = item[0]
    str_operand = str(operand)
    space_size = problem_sizes[index] - get_digit_count(operand)

    f_line = f_line + " " * space_size + str_operand
    if index != len(sub_problems) - 1:
      f_line = f_line + problem_space

  # Format second line
  for index, item in enumerate(sub_problems):
    operand = item[1]
    str_operand = str(operand)
    operator = item[2]
    space_size = problem_sizes[index] - get_digit_count(operand) - 1

    s_line = s_line + operator + " " * space_size + str_operand
    if index != len(sub_problems) - 1:
      s_line = s_line + problem_space

  # Format dash line
  for index, item in enumerate(sub_problems):
    problem_size = problem_sizes[index]

    d_line = d_line + "-" * problem_size
    if index != len(sub_problems) - 1:
      d_line = d_line + problem_space

  # Format solution line
  if solutions is True:
    for index, item in enumerate(sub_problems):
      solution = item[3]
      str_solution = str(solution)
      # Account for negative numbers taking an extra space
      if solution > 0:
        space_size = problem_sizes[index] - get_digit_count(solution)
      else:
        space_size = problem_sizes[index] - get_digit_count(solution) - 1

      sol_line = sol_line + " " * space_size + str_solution
      if index != len(sub_problems) - 1:
        sol_line = sol_line + problem_space

  # Create final formatted string to return
  if solutions is True:
    arranged_problems = f'{f_line}\n{s_line}\n{d_line}\n{sol_line}'
  else:
    arranged_problems = f'{f_line}\n{s_line}\n{d_line}'

  return arranged_problems


# Return digit count of input number
def get_digit_count(n):
  if n < 0:
    n = -n  # Convert negative integer to positive
  digit_str = str(n)
  return len(digit_str)


# Return number of whitespaces needed for a problem
def get_problem_size(num1, num2):
  count_1 = get_digit_count(num1)
  count_2 = get_digit_count(num2)
  if count_1 > count_2:
    return count_1
  return count_2
