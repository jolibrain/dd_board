# dd_board
Version 0.3

Works with: Python 2.7

Version 0.3
Converts logs to "TensorBoard compatible" data.

Parameters:
- log_src = string, log source to analyze
- tb_dir = string, cache directory used by tensorboard
- del_dir = bolean, False if ommited. If set to false, the new graph is displayed after the preceding, if any. If set to true, the tensorboard cache directory will be deleted and the new graph will be the only one to appear.

Requirements:
-------------

- [tensorboard_logger](https://github.com/TeamHG-Memex/tensorboard_logger)

Usage:
------

```
from dd_board_logger import DDBoard

do_what_have_to_be_done_before()

read_dd = DDBoard(tb_dir, del_dir)
```

Then, with a log flow:
```
read_dd.ddb_logger(log_src)
```

Or, with a log file:
```
read_dd.ddb_logger_file(log_src)
```

Or with external data (need "import json, time", for this example):
```
log_src = open(json_src, 'r')
for line in log_src:

json_src = open(log_src, 'r')
for line in json_src:
	json_obj = json.loads(line)
	read_dd.ddb_logger(json_obj)
	time.sleep(1)
```

You can then start TensorBoard in console:
```
$tensorboard --logdir tb_dir
```
