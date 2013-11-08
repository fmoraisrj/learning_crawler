#! _*_ encoding: utf-8 _*_

fruits = ["banana", "jaca", "pera", "maçã", "fe"]

i = 0
while i < len(fruits):
	if len(fruits[i]) < 3:
		fruits.remove(fruits[i])
		print fruits
	i += 1