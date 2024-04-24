import math
def paint_area_calculator(height,width,coverage):
	num_of_cans = (height*width)/coverage
	num_of_cans = math.ceil(num_of_cans)
	print(num_of_cans)

test_h = int(input("Enter the Height: "))
test_w = int(input("Enter the Width: "))
cover = 5

paint_area_calculator(height = test_h, width = test_w, coverage = cover)