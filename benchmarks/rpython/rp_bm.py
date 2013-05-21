from rp_call_bm import *
from rp_syscall_bm import *
from rp_fannkuch_bm import *
import rp_binary_trees_bm
import rp_fasta_bm
import rp_float_bm
import rp_go_bm
import rp_nbody_bm
import rp_stringlist_bm
import rp_threading_bm

def main(argv):
	i = int(argv[1])
	n = 10
	if (i == 1):
		rp_call_bm.boot(n)
	elif (i == 2):
		rp_syscall_bm.boot(n)
	elif (i == 3):
		rp_fannkuch_bm.boot(n)
	elif (i == 4):
		rp_binary_trees_bm.boot(n)
	elif (i == 5):
		rp_fasta_bm.boot(n)
	elif (i == 6):
		rp_float_bm.boot(n)
	elif (i == 7):
		rp_go_bm.boot(n)
	elif (i == 8):
		rp_nbody_bm.boot(n)
	elif (i == 9):
		rp_stringlist_bm.boot(n)
	elif (i == 10):
		rp_threading_bm.boot(n)
	return 0



def target(driver,args):
    return main,None

