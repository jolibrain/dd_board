# dd_board
Version 0.4

Works with: Python 2.7

Converts logs to "TensorBoard compatible" data.

Parameters (except for del_dir, they must be written between quotes, even if left empty):
- log_src = string, log source to analyze (flow, log file or any Python dict / JSON object).
- base_dir = string, general cache directory used by tensorboard. If not existing, will be created.
- sub_dir = string, subdirectory of the current run used by tensorboard. If not existing, will be created.
- del_dir = bolean, *False* if ommited. If set to *False*, the new graph is displayed after the preceding one, if any. If set to *True*, the tensorboard cache directory (*base_dir/sub_dir*) will be deleted and the new graph will be the only one to appear.

Requirements:
-------------

- [tensorboard_logger](https://github.com/TeamHG-Memex/tensorboard_logger)

Usage:
------

```
from dd_board_logger import DDBoard

do_what_have_to_be_done_before()

read_dd = DDBoard(base_dir, sub_dir, del_dir)
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
$tensorboard --logdir base_dir

```
(base_dir without quotes, here. Ex: *tensorboard --logdir runs*)
