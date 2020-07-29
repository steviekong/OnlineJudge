from django.contrib.auth.hashers import BCryptPasswordHasher

class MyBCryptPasswordHasher(BCryptPasswordHasher):
	#Reducing bcrypt hashing to 10 rounds
	rounds = 10