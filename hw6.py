# Определить значение функции Z = 1 / (XY) при X и Y не равных 0.
nx =  input ( " Введите число x " )
nx =  int (nx)
ny =  input ( " Введите число y " )
ny =  int (ny)
если nx ==  0  или ny ==  0 :
    print ( " Значения не должны быть равны 0, проверьте данные " )
еще : Z =  1 / (nx * ny)
print ( " Значение функции = " , Z)
