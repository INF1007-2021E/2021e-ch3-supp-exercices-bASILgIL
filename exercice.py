#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	"""a = ("La puissance dissipée par la résistance est de", str(round(voltage**2/resistance, 2)),"W.")
	separateur = " "
	return separateur.join(a)"""
	return (voltage**2 * resistance)

def orthogonal(v1, v2):
	return (v1[0]*v2[0] + v1[1]*v2[1]) == 0


def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	new = []
	for v in values:
		if v >= 0:
			new.append(v)
	return sum(new)/len(new)
		 # La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties, tens, fives, twos, ones = 0, 0, 0, 0, 0
	while value != 0:
		if value >= 20:
			twenties = value//20
			value = value - twenties * 20
		elif value >= 10:
			tens = value//10
			value = value - tens * 10
		elif value >= 5:
			fives = value//5
			value = value - fives * 5
		elif value >= 2:
			twos = value//2
			value = value - twos * 2
		elif value >= 1:
			ones = value


	return (twenties, tens, fives, twos, ones)

if __name__ == "__main__":


	print(dissipated_power(69, 420))
	print(dissipated_power(42, 9000))
	print(orthogonal((0, 1), (-1, 1)))
	print(average([1, 4, -1, 10]))
	print(average([1, 4, -1, 10, 0]))
	print(average([-12, -42, 1]))
	print(average([0xDEAD, 0xBEEF, 420, 69]))
	print(bills(0xDEAD))


