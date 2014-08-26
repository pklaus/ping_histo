
## ping\_histo – creating histograms from ping times

This is a wrapper to call `ping` from Python and
continuously parse its output.
It can extract the ping times and thus simplifies drawing histograms
or calculating your own metrics based on `ping`'s output.

### Requirements

Tested with Python 2.7 and 3.3.
Not guaranteed to work however!

No other Python modules required.

The `ping` command must be available.

### ToDo

* Adding support for IPv6
* Adding support for more versions of ping (Debian, Ubuntu, Arch, Mac OS X)
* Histogram in Terminal output or just data?
* Add support for signals if continously pinging:
  * To terminate
  * To print current statistics?
* Show a histogram (via matplotlib) and update it continuously.
  This requires a change to the code structure and adding a new CLI option.

### Drawing the histogram

Drawing the histogram is currently not included in this tool.
This tool just creates the output for other tools to display the data.

You can check [this question on Stackoverflow](http://stackoverflow.com/q/6949332/183995)
for ideas of what tools to use.

#### Using together with `histogram.py`

This tool may be used together with `histogram.py`
from [data-hacks](https://github.com/bitly/data_hacks)
(install using `pip install data_hacks`):

    ./ping_histo.py 192.168.1.1 -c 50 | histogram.py

(Data\_hacks does currently NOT work with Python 3.)

