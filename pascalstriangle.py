def pascal_triangle(rows):
  """
  Generates Pascal's triangle for a given number of rows.

  Args:
      rows: The number of rows in the triangle.

  Returns:
      A list of lists representing Pascal's triangle.
  """
  triangle = []

  # Create the first row with a 1
  triangle.append([1])

  # Iterate through the remaining rows
  for i in range(1, rows):
    # Create a new row with the first element as 1
    new_row = [1]

    # Calculate the remaining elements using the previous row
    for j in range(1, i):
      previous_row = triangle[i - 1]
      new_row.append(previous_row[j - 1] + previous_row[j])

    # Add the last element as 1
    new_row.append(1)

    # Append the new row to the triangle
    triangle.append(new_row)

  return triangle

# Example usage
rows = 6
triangle = pascal_triangle(rows)

# Print the triangle
for row in triangle:
  print(row)
