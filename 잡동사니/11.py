def solution(t, r):
	answer = []
	max_time = max(t)
	waiting = [0 for _ in range(len(t))]

	for i in range(max_time+len(r)):
		for j in range(len(t)):
			if t[j] == i:
				waiting[j] = 1

		lift = 0
		for i in range(len(waiting)):
			if waiting[i] == 1:
				lift = i
				break

		for j in range(1, len(waiting)):
			if waiting[j] == 1:
				if r[j] < r[lift]:
					lift = j
				elif r[j] == r[lift]:
					if t[j] < t[lift]:
						lift = j
					elif t[j] == t[lift]:
						if j < lift:
							lift = j

		if waiting.count(1) > 0 :
			answer.append(lift)
		waiting[lift] = 0

	return answer

solution([0, 1, 3, 0], [0, 1, 2, 3])
# solution([1,1,1,1,1], [0,0,0,0,0])
