

def main():
	n = 10
	files = ["rp_call_bm", "rp_fannkuch_bm", "rp_binary_trees_bm", "rp_fasta_bm", "rp_float_bm", "rp_go_bm", "rp_nbody_pm"]
	for curFile in files:
		pm =__import__(curFile)
		print ""
		pm.boot(10)


main()
