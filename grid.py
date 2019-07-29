import os, sys, fnmatch
#import well

class Grid(object):
	def __init__(self, args, grid_path, new_grid_path):
		self.args = args
		self.grid_dir_path = grid_path
		self.new_grid_dir_path = new_grid_path
		
		self.create_grid_directories()
		self.create_frame_directories()
		
	
	def create_grid_directories(self):	
		# Create a mesterfile directory:
		try:
			os.makedirs(self.new_grid_dir_path)
		except OSError:
			print("Creation of the directory (path:{}) failed.".format(self.new_grid_dir_path))
		else:
			print("Successfully created the directory (path:{})".format(self.new_grid_dir_path))
			
			
		
	def create_frame_directories(self):
		cdf_files = fnmatch.filter(os.listdir(self.grid_dir_path), '*.cbf')
		#print(cdf_files)
		
		temporary_list = []
		grid_dir_name_list = []	
			
		number = range(1, len(cdf_files), 15)
		for num in number:
			temporary_list.append(cdf_files[num])
		#print(temporary_list)
		
		for each in temporary_list:
			end_index = each.find('_phi')
			start_index = each.rfind('grid_*')
			dir_name = each[start_index+8:end_index]
			grid_dir_name_list.append(dir_name)
		#print(grid_dir_name_list)
			
			
		for each in grid_dir_name_list:
			new_path = '{}/{}'.format(self.new_grid_dir_path, each)
			#print(new_path)
			try:
				os.makedirs(new_path)
			except OSError:
				print("Creation of the directory (path:{}) failed.".format(new_path))
			else:
				print("Successfully created the directory (path:{})".format(new_path))
