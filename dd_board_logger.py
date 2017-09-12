# -*- coding:utf-8 -*-
import json, os
from shutil import rmtree
from datetime import datetime
from tensorboard_logger import configure as tbl_configure, log_value as tbl_log_value

class DDBoard:
	"""Version 0.4
	Converts logs to "TensorBoard compatible" data."""
	
	# Default values
	base_dir = "/opt/tensorboard/runs" # useful to have a default?
	#~ flush_time = 2 # Really needed? tb apparently refreshes/flushes its cache after each event written. See at the end of the __init__ part.

	def __init__(self, base_dir, sub_dir, del_dir = False):
		"""
			- base_dir = string, general cache directory used by tensorboard
			- sub_dir = string, subdirectory of the current run used by tensorboard
			- del_dir = bolean, False if ommited. If set to false, the new graph is displayed after the preceding, if any. If set to true, the tensorboard cache directory will be deleted and the new graph will be the only one to appear.
			- flush_time = interval between 2 flushes of tb cache.
		"""

		if base_dir != "":
			self.base_dir = base_dir
		else:
			self.base_dir = DDBoard.base_dir

		if sub_dir != "":
			self.sub_dir = sub_dir
		else:
			self.sub_dir = "/run-" + datetime.now().strftime('%y%m%d-%H%M%S')
		
		self.run_dir = self.base_dir + "/" + self.sub_dir
		
		if (del_dir):
			if (os.path.isdir(self.run_dir)):
				rmtree(self.run_dir) # cleaning of the tb run directory

		#~ if ft != "": # To be deleted if tb flushtime is finally not taken in account
			#~ self.flush_time = ft
		#~ else:
			#~ self.flush_time = DDBoard.flush_time
			
		#~ tbl_configure(self.run_dir, flush_secs=DDBoard.flush_time)
		tbl_configure(self.run_dir)

	def ddb_logger(self, obs):
		"""obs = the Python dict (aka JSON object) to be analyzed.""" 
		for key in obs.keys():	
				if (key != "iteration"):
						value = obs[key]
						tbl_log_value(key, obs[key], int(obs["iteration"]))
						
	def ddb_logger_file(self,json_file):
		"""json_file = the json file to be analyzed"""
		json_src = open(json_file, 'r') # Should we check the existence of the JSon source?
		for line in json_src:
			json_line = json.loads(line)
			self.ddb_logger(json_line)
