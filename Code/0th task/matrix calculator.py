def create_matrix():
    rownum=int(input("Enter number of rows: "))
    colnum=int(input("Enter number of columns: "))
    matrix=[]
    for i in range(rownum):
        row=[]
        for j in range(colnum):
            value = int(input(f"Enter element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def display(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:4}", end=" ")
        print()


def matsum(mat1,mat2):
    if len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0]):
        print("Matrices must have the same dimensions!")
        return None
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]+mat2[i][j])
        result.append(row)
    return result


def matsub(mat1,mat2):
    if len(mat1) != len(mat2) or len(mat1[0])!=len(mat2[0]):
        print("Matrices must have the same dimensions!")
        return None
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]-mat2[i][j])
        result.append(row)
    return result


def matmul(mat1, mat2):
    if len(mat1[0])!=len(mat2):
        print("Number of columns of the first matrix must equal number of rows of the second matrix!")
        return None
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat2[0])):
            total=0
            for k in range(len(mat2)):
                total+=mat1[i][k]*mat2[k][j]
            row.append(total)
        result.append(row)
    return result


def scalarsum(mat1,a):
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]+a)
        result.append(row)
    return result


def scalarmul(mat1,x):
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]*x)
        result.append(row)
    return result


def matnorm(mat1):
    minval=mat1[0][0]
    maxval=mat1[0][0]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if mat1[i][j]>maxval:
                maxval=mat1[i][j]
            if mat1[i][j]<minval:
                minval=mat1[i][j]
    if minval==maxval:
        print("Error! Division by zero!")
        return None
    result = []
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append((mat1[i][j]-minval)/(maxval-minval))
        result.append(row)
    return result


def main():
    print("Welcome to matrix calculator \n----------------------------")
    op=int(input("""    1- Addition 
    2- Subtraction 
    3- Multiplication 
    4- Scalar summation 
    5- scalar multiplication
    6- Normalization
    
    Choose an operation (pick a number): """))

    if op in range(1,4):
        print("First matrix")
        mat1 = create_matrix()
        print("Second matrix")
        mat2 = create_matrix()
        print("\nFirst matrix:")
        display(mat1)
        print("\nSecond matrix:")
        display(mat2)

        if op == 1:
            print("\nResult of addition:")
            display(matsum(mat1, mat2))

        elif op == 2:
            print("\nResult of subtraction:")
            display(matsub(mat1,mat2))

        elif op == 3:
            print("\nResult of multiplication:")
            display(matmul(mat1, mat2))

    elif op in range(4,7):
        print("Enter your matrix")
        mat1 = create_matrix()
        print(f"Your matrix is: {mat1}")

        if op == 4:
            a = int(input("Enter the addition scalar quantity: "))
            print("\nResult of scalar addition:")
            display(scalarsum(mat1, a))

        elif op == 5:
            x = int(input("Enter the multiplication scalar quantity: "))
            print("\nResult of scalar maltiplication:")
            display(scalarmul(mat1, x))

        elif op == 6:
            print("\nResult of linear normalization:")
            display(matnorm(mat1))
    else:
        print("Please enter a number from 1 to 6")

if __name__=="__main__":
    main()






 







