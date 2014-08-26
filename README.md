
## ping-histogram

This is a wrapper to call `ping` from Python and
continuously parse its output.
It can extract ping times and let you draw histograms
or calculate your own metrics based on the `ping`'s output.

### Requirements

Tested with Python 2.7 and 3.3.
Not guaranteed to work however!

Needs to be able to call the `ping` command.

No other Python modules required.

### ToDo

* Add support for signals if continously pinging:
  * To terminate
  * To print current statistics?
* Histogram in Terminal output or just data?

### Drawing the histogram

Drawing the histogram is not included in this tool.
This tool just creates the output for other tools
to display the data.

You can check [this question on Stackoverflow](http://stackoverflow.com/q/6949332/183995)
for ideas of what tools to use.

#### Using together with `histogram.py`

This tool may be used together with `histogram.py`
from [data-hacks](https://github.com/bitly/data_hacks)
(install using `pip install data_hacks`):

    ./ping_histo.py 192.168.1.1 -c 50 | histogram.py

