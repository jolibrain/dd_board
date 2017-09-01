# -*- coding:utf-8 -*-
import json, sys, os
from datetime import datetime
from tensorboard_logger import configure as tsbl_configure, log_value as tsbl_log_value

class DDBoard:
	"""Version 0.1
	Converts a log to "TensorBoard compatible" data.
	- log_file = log file used for the graph
	- run_dir = directory used by tensorboard logger
	- flush_time = interval between 2 flushes of the log file
	"""

	# Default values, if needed
	log_file = "mobilenet_ilsvrc_cleaned.log"
	run_dir = "runs/run-"
	flush_time = 3

	def __init__(self, lf, rd, ft):
		#~ print(self.log_file, self.run_dir, self.flush_time)
		if lf != "":
			self.log_file = lf
		else:
			self.log_file = DDBoard.log_file

		if rd != "":
			if os.path.isdir(rd):
				new_rd = rd + "-" + datetime.now().strftime('%y%m%d-%H%M%S')
				print("{0} already existing. Creating {1} instead...".format(rd, new_rd))
				self.run_dir = new_rd
			else:
				self.run_dir = rd
		else:
			self.run_dir = DDBoard.run_dir + datetime.now().strftime('%y%m%d-%H%M%S')

		if ft != "":
			self.flush_time = ft
		else:
			self.flush_time = DDBoard.flush_time

	def ddb_logger(self):
		tsbl_configure(self.run_dir, flush_secs=self.flush_time)

		try:
			log_file = open(self.log_file, 'r')
		except IOError:
			print ("Does {0} exist?".format(self.log_file))
			sys.exit()

		print("Converting data...")
		for line in log_file:
			jsonLine = json.loads(line)
			for key in jsonLine.keys():
				if (key != "iteration"):
					value = jsonLine[key]
					tsbl_log_value(key, jsonLine[key], int(jsonLine["iteration"]))
