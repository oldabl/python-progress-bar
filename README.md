# Python Progress Bar
Prints an all customisable **easy-to-use** progress bar. It can be the thread target or a normal function call.


## Import in your code
```python
from *folderclone*.ProgressBar import ProgressBar
```
Now use as class ProgressBar.
/!\ folderclone should not contain character "-". Make sure not to clone in default git clone dir for this repo.


## Use
### As a simple function call
```python
max = 30
progressbar = ProgressBar()
for n in range(0,max):
  progressbar.print(n,max-1)
  time.sleep(1) # To see progress
```

### As a separate thread target (adds 7 lines to your code)
```python
max = 30
progressbar = ProgressBar()
number = multiprocessing.Value("i", 0)
pr = multiprocessing.Process(target=progressbar.inThread, args=(number,max-1))
pr.start()
# YOUR CODE GOES BELOW
# It needs to increment the ProgressBar number
for n in range(0,max)
  number.value = n
  time.sleep(1)
# YOUR CODE GOES ABOVE
pr.join() # or pr.kill()
```


## Go further: customise your bar
### Style parameters
You can give the following optional arguments to the ProgressBar constructor:
- pretext: Text to print before the bar (default "")
- progresschar: Character to show progress (default '█')
- remainingbarchar: Character to fill the remaining bar with (default ' ')
- loadingchars: Last character of bar moving as bar loads (moves even if no progress) (default "█▓▒░▒▓")
- startendchar: The two characters going around the bar (default "||")
- displaypercentage: Show percentage as well or not (default False)
- displaycount: Show count as well or not (default False)
- rightjustified: Print the bar on the right hand side of the console (default True)
- consolewidthrate: Choose the section the bar occupies on the console (default 3 => 1/3 of the console)
### Thread parameters
If you use the thread version, you can customise the refresh time of your progress bar.
To do this, give an extra argument (type float) representing the refreshing period of the bar.
```python
multiprocessing.Process(target=progressbar.inThread, args=(number,max,0.2))
```
