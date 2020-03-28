

C, N, M = map(int, input().split())
# C = Max number of cows allowed on farm
# N = number of initial farms
# M = number of different days that the regulator visits.

farms = [int(input()) for i in range(N)]
farms_copy = farms[:]

days = [int(input()) for i in range(M)]

will_double = 0

def day_pass(farms, will_double):
	for farm in range(len(farms)):
		farms[farm] *= 2
	return will_double * 2, farms

def get_will_double(farms, will_double, C):
	new_farms = []
	for farm in range(len(farms)):
		if farms[farm] * 2 > C:
			will_double += 1
		else:
			new_farms.append(farms[farm])
	return will_double, new_farms

for day in days:
	farms = farms_copy[:]
	will_double = 0
	current_day=0
	while current_day != day:
		will_double, farms = get_will_double(farms, will_double, C)
		will_double, farms = day_pass(farms, will_double)
		current_day+=1
	print(len(farms) + will_double)
