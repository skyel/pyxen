import time

class rp_syscall_bm:
	@staticmethod
	def test_calls():
		number_of_calls = 6400000
		val = 0
		t0 = time.time()
		for _ in xrange(number_of_calls):
			val = val + time.time()
		t1 = time.time()
		return t1 - t0

	@staticmethod
	def	 rp_syscall_main(n):
		print "==Syscall benchmark=="
		iterations=int(n)
		for i in xrange(iterations):
			print str(i) + ": " + str(rp_syscall_bm.test_calls())
		return 0

	@staticmethod
	def	 boot(n):
		rp_syscall_bm.rp_syscall_main(n)
