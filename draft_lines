import argparse, os, sys, fnmatch, time
import grid

def main():
	time1=time.time()
	parser = argparse.ArgumentParser(description='Argument required to process data: input path')
	parser.add_argument('-i', '--input', type=str, nargs='+', required=True, help='Path to the data directory')
	parser.add_argument('--output', default=os.getcwd(), help='Use this option to change output directly')
	parser.parse_args()

	args = parser.parse_args()
	
	# Find grid directories and make a list of them:
	for directory in args.input:
		grids_list = fnmatch.filter(os.listdir(directory), 'grid*')
		#print(grids_list)
		for grid_directory in grids_list:
			grid_path = "{}/{}".format(directory, grid_directory)
			new_grid_path = "{}/{}".format(args.output, grid_directory)
			grid_class = grid.Grid(args, grid_path, new_grid_path)

		
	time2 = time.time()
	print("Total time: {:.1f} s".format(time2-time1))
	
if __name__=='__main__':
	main()
