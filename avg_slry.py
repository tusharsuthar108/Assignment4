def average_salary_excluding_min_max(salary):

  if len(salary) < 3:
    raise ValueError("Array must have at least 3 elements.")

  min_salary = min(salary)
  max_salary = max(salary)

  total_salary = sum(salary) - min_salary - max_salary
  num_employees = len(salary) - 2

  return total_salary / num_employees

salary = [4000, 3000, 1000, 2000]
average_salary = average_salary_excluding_min_max(salary)
print(average_salary)
