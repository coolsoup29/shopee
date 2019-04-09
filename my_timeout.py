import time,os,signal,functools

TIME_NAME=time.ctime().split(" ")
for i in TIME_NAME:
	if i == "":
		TIME_NAME.remove("")

if TIME_NAME[1] in ['Jan','Feb','Mar']:
	DIR_NAME=1
elif TIME_NAME[1] in ['Apr','May','Jun']:
	DIR_NAME=2
elif TIME_NAME[1] in ['Jul','Aug','Sep']:
	DIR_NAME=3
elif TIME_NAME[1] in ['Oct','Nov','Dec']:
	DIR_NAME=4
# SEASON NUM

#DATA_TIME = 'Jan16'
DATA_TIME=TIME_NAME[1]+TIME_NAME[2]
# try:
# 	os.system("mkdir %s"%DIR_NAME)
# except Exception:
# 	pass


# with open("./%s/fg_coolsoup.txt"%DIR_NAME,"a",encoding="utf-8") as f:
#     f.write("this is my test for dir_NAME\n")
#
#
# class TimeoutError(Exception): pass
#
#
# def timeout(seconds, error_message="Timeout Error: the cmd 5s have not finished."):
# 	def decorated(func):
# 		result = ""
#
# 		def _handle_timeout(signum, frame):
# 			global result
# 			result = error_message
# 			raise TimeoutError(error_message)
#
# 		def wrapper(*args, **kwargs):
# 			global result
# 			signal.signal(signal.SIGALRM, _handle_timeout)
# 			signal.alarm(seconds)
#
# 			try:
# 				result = func(*args, **kwargs)
# 			finally:
# 				signal.alarm(0)
# 				# return result
# 			return result
#
# 		return functools.wraps(func)(wrapper)
#
# 	return decorated
