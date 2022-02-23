import random,os,string

def password_generator(passlen,bits=4096,char=string.ascii_letters+string.digits+string.punctuation):
	return "".join([random.SystemRandom(os.urandom(bits)).choices(char,k=passlen)[random.SystemRandom(os.urandom(bits)).randint(0,passlen-1)] for _ in range(passlen)])
