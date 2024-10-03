def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Create a row filled with 1s
        for j in range(1, i):  # Calculate inner elements
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Append the completed row to the triangle
    
    return triangle
