def triangle(n):
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])  
        else:
            row = [1]  
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)  
            triangle.append(row)
    return triangle

def write_triangle(triangle, filename):
    with open(filename, 'w') as filout:
        for row in triangle:
            filout.write(' '.join(map(str, row)) + '\n')

pascal_triangle = triangle(10)
write_triangle(pascal_triangle, 'zoo2.txt')