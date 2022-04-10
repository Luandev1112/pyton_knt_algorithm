def AverageHeight(datas):
	total = 0
	for i in range(0, len(datas)):
		total += int(datas[i][3])
	avg = int(total/len(datas))
	return avg

def ArrangeRow(datalist):
	datalist = SortbyVertical(datalist)
	row_arr = []
	row = []
	avg_height = AverageHeight(datalist) /2
	row.append(datalist[0])
	if(len(datalist) == 1):
		row_arr.append(row)
	elif len(datalist) > 1:
		for i in range(1, len(datalist)):
			current_data = datalist[i]
			prev_data = datalist[i - 1]
			if int(current_data[1]) + int(current_data[3]) - int(prev_data[1]) - int(prev_data[3]) < avg_height :
				row.append(current_data)
			else:
				row_arr.append(row)
				row = []
				row.append(current_data)
			if(i == len(datalist) - 1):
				row_arr.append(row)
		
	return row_arr 

def SortbyVertical(datalist):
	for i in range(0, len(datalist) - 1):
		for j in range(i + 1, len(datalist)):
			i_data_arr = datalist[i]
			j_data_arr = datalist[j]
			if float(i_data_arr[1]) > float(j_data_arr[1]):
				tmp = datalist[i]
				datalist[i] = datalist[j]
				datalist[j] = tmp     
	return datalist

def ArrangeColumn(row_arr):
    for i in range(0, len(row_arr) - 1):
        for j in range(i + 1, len(row_arr)):
            i_data_arr = row_arr[i]
            j_data_arr = row_arr[j]
            if float(i_data_arr[0]) > float(j_data_arr[0]):
                tmp = row_arr[i]
                row_arr[i] = row_arr[j]
                row_arr[j] = tmp     
    return row_arr

def ArrangeBoxes(cols):
	group_arr = []
	group = cols[0]
	if len(cols) > 1 :
		for i in range(1, len(cols)):
			col = cols[i]
			prev = cols[i-1]
			if group[4] == col[4] and col[0] - prev[0] < col[2] + prev[2]:
				group[2] = col[0] - group[0] + col[2]
				if group[3] < col[3]:
					group[3] = col[3]
				if group[1] > col[1]:
					group[1] = col[1]
			else:
				group_arr.append(group)
				group = col
			if i == len(cols) - 1:
				group_arr.append(group)
	else:
		group_arr.append(group)	
	return group_arr

def getPlanogramBlock(planogram, val):
	block = []
	for plano in planogram:
		if val == plano[0]:
			block = plano
			break
		else:
			continue
	str_block = [str(int) for int in block]
	return str_block

def getPlanogramPossiblity(cols, planogram):
	str_plano_arr = []
	if len(cols) > 2:
		for i in range(0, len(cols) - 2):
			col_1 = cols[i]
			col_2 = cols[i+1]
			col_3 = cols[i+2]
			block_1 = getPlanogramBlock(planogram, col_1[4])
			block_2 = getPlanogramBlock(planogram, col_2[4])
			block_3 = getPlanogramBlock(planogram, col_3[4])
			if col_1[4] == col_2[4] or col_2[4] == col_3[4] or col_1[4] == col_3[4]:
				continue

			if len(block_1) == 0 or len(block_2) == 0 or len(block_3) == 0:
				continue
			str_plano = ','.join(block_1) + ',' + ','.join(block_2) + ',' + ','.join(block_3)
			str_plano_arr.append(str_plano)
	return str_plano_arr

def colsToStr(cols):
	result = ''
	i = 0
	for col in cols:
		i += 1
		result += str(col[4])
		if i < len(cols):
			result += ','
	return result

def checkPlanoStr(strCols, str_planos):
	result = False
	for strplano in str_planos:
		pos = strCols.find(strplano)
		if pos >= 0:
			result = True
			break;
	return result


boxes = [[116, 34, 50, 104, 6], [219, 51, 50, 83, 6], [185, 52, 47, 81, 6], [155, 53, 46, 80, 6], [341, 181, 40, 109, 8], [157, 188, 45, 97, 8], [120, 188, 46, 93, 11], [88, 197, 42, 95, 11], [368, 188, 33, 86, 12], [325, 188, 30, 79, 11], [217, 188, 38, 74, 11], [268, 188, 38, 74, 11], [296, 188, 32, 70, 11], [59, 188, 42, 69, 11], [246, 188, 32, 57, 11], [195, 188, 34, 54, 11], [316, 188, 29, 95, 2], [132, 188, 36, 103, 16], [188, 188, 38, 96, 16], [242, 188, 34, 94, 16], [364, 188, 26, 80, 2], [266, 188, 33, 90, 16], [293, 188, 29, 83, 2], [159, 188, 37, 97, 16], [341, 335, 27, 77, 2], [215, 336, 35, 90, 16], [101, 188, 39, 97, 16], [383, 188, 35, 73, 14], [71, 380, 39, 61, 16], [376, 462, 33, 74, 7], [354, 479, 28, 63, 7], [158, 480, 31, 86, 0], [131, 481, 38, 91, 1], [335, 556, 34, 83, 2]]
planogram = [[6,6,6],[8],[7,7],[11],[2],[16,16],[0,0]]
rows = ArrangeRow(boxes)
planocount = 0
for row in rows:
	cols = ArrangeColumn(row)
	groups = ArrangeBoxes(cols)
	str_planos = getPlanogramPossiblity(groups, planogram)
	strCols = colsToStr(cols)
	if checkPlanoStr(strCols, str_planos):
		planocount += 1
print(planocount)