# -*- coding:utf-8 -*-
import json, os
from shutil import rmtree
from datetime import datetime
from tensorboard_logger import configure as tbl_configure, log_value as tbl_log_value

class DDBoard:
	"""Version 0.3
	Converts logs to "TensorBoard compatible" data.
	- obs = data flow that has to be analyzed
	- json_file = log file (if any) to be analyzed
	- tb_dir = directory used by tensorboard logger
	- flush_time = interval between 2 flushes of tb cache
	"""
	
	# Default values
	tb_dir = "/opt/tensorboard/runs" # useful to have a default?
	flush_time = 2 # if needed? tb apparently refreshes/flushes its cache after each event written.

	def __init__(self, base_dir, del_dir = False):
		if base_dir != "":
			self.tb_dir = base_dir
		else:
			self.tb_dir = DDBoard.tb_dir
			
		self.comp_dir = "/run-" + datetime.now().strftime('%y%m%d-%H%M%S')
		
		if (del_dir):
			if (os.path.isdir(self.tb_dir)):
				rmtree(self.tb_dir) # cleaning of the tb run directory
		else:
			if (os.path.isdir(self.tb_dir)):
				self.comp_dir = "/" + os.listdir(self.tb_dir)[0]

		self.run_dir = self.tb_dir + self.comp_dir

		#~ if ft != "": # To be deleted if tb flushtime is finally not taken in account
			#~ self.flush_time = ft
		#~ else:
			#~ self.flush_time = DDBoard.flush_time
			
		#~ tbl_configure(self.run_dir, flush_secs=DDBoard.flush_time)
		tbl_configure(self.run_dir)

	def ddb_logger(self, obs):
		for key in obs.keys():	
				if (key != "iteration"):
						value = obs[key]
						tbl_log_value(key, obs[key], int(obs["iteration"]))
						
	def ddb_logger_file(self,json_file):
		json_src = open(json_file, 'r') # Should we check the existence of the JSon source?
		for line in json_src:
			json_line = json.loads(line)
			self.ddb_logger(json_line)
