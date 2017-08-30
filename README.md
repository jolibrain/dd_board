# dd_board
Version 0.9
Works with: Python 2.7

Converts a log to "TensorBoard compatible" data.
Variables:

- log_file = log file used for the graph
- run_dir = directory used by tensorboard logger
- flush_time = interval between 2 flushes of the log file


Requirements:
-------------

- [tensorboard_logger](https://github.com/TeamHG-Memex/tensorboard_logger)

Usage:
------
rlog = DDBoard(log_file,run_dir,flush_time)

```
from dd_board_logger import DDBoard

[...]

rlog = DDBoard("logfile.log","runs/run-1234",3)
rlog.ddb_logger()

```

You can start TensorBoard right away:
tensorboard --logdir runs
