def make_zeroes(matrix):
  # TODO: Write - Your - Code

  z_list = scan(matrix)
  
  for x in range(len(z_list)):
    
    matrix = zero(matrix,z_list[x][0], z_list[x][1])

  return matrix


def scan(matrix):
  zero_list = []
  for x in range(len(matrix)):
    for i in range(len(matrix[x])):
      if matrix[x][i] == 0:
        zero_list.append([x,i])
  
  return zero_list;


def zero(matrix, x, i ):

    for m in range(len(matrix)):
        matrix[m][i] = 0
    
    for n in range(len(matrix[x])):
        matrix[x][n] = 0


    return matrix










arr1= [[1,2,3,4,0], [1,2,3,2,1], [1,2,3,4,2], [1,0,2,3,4]]

print( make_zeroes(arr1))
