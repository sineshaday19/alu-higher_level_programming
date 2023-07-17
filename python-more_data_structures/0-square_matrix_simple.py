#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #Create a new matrix 
    result_matrix = []
    # Iterate over each row in the input matrix
    for row in matrix:
        #Create a new row for the result matrix
        squared_row = []
        #Iterate over each element in the current row
        for element in row:
            #Compute the square 
            squared_row.append(element ** 2)
        #Append the squared row to the result matrix
        result_matrix.append(squared_row)
    return result_matrix
