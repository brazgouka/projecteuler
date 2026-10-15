from math import factorial

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def p24(n = 1_000_000):
	out = ""
	seg_length = factorial(len(digits)) / len(digits)
	current_element = 1
	prev_sum = 0
	while digits:
		if current_element * seg_length + prev_sum < n:
			current_element += 1
			continue
		prev_sum += (current_element - 1) * seg_length
		out += digits.pop(current_element - 1)
		current_element = 1
		seg_length = factorial(len(digits)) / len(digits) if digits else 0
	return out
	

print(p24())
