import time, sys, os

# Class: ProgressBar
# Role: print a progress bar with next to no
#  line of code required by user
class ProgressBar:

  # Role : assign arguments to internal values
  def __init__(self,
              pretext=r"", # Text to print before the bar
              progresschar=r"█", # Character to show progress
              remainingbarchar=r" ", # Character to fill the remaining bar with
              loadingchars=r"█▓▒░▒▓", # Last character of bar moving as bar loads (moves even if no progress)
              startendchar=r"||", # The two characters going around the bar
              barwidth=int(os.get_terminal_size().columns/2), # Length of the bar in characters (does not include what's around the bar)
              displaypercentage=False, # Show percentage as well or not
              displaycount=False # Show count as well or not
              ):
    self.pretext = str(pretext)
    self.progresschar = str(progresschar)
    self.remainingbarchar = str(remainingbarchar)
    self.loadingchars = loadingchars
    self.startendchar = str(startendchar)
    self.barwidth = int(barwidth)
    self.displaypercentage = displaypercentage
    self.displaycount = displaycount

    # Private
    self.loadingcharsindex = 0
    self.firstprint = True

  
  # Role : prints the progress bar as an independent thread
  # Arguments:
  # - number: progress value (type multiprocessing.Value of int)
  # - max: value to reach (int)
  # - updateperiod: refresh period of progress bar in seconds
  def inThread(self, number, max, updateperiod=0.1):
    while(number.value != max):
      self.print(number.value,max)
      time.sleep(float(updateperiod))
    self.print(max,max)

  
  # Role : prints the progress bar inline
  # Arguments:
  # - number: progress value (int)
  # - max: maximum value (int)
  def print(self,number,max):
    barstring = ""

    # No carriage return on first print
    if not self.firstprint:
      barstring += "\r"
    self.firstprint = False

    # Pre progress bar
    if self.pretext:
      barstring += self.pretext

    # Progress bar
    #
    # Start char
    if self.startendchar:
      barstring += self.startendchar[0]
    # Current state of affairs
    sofarbar = int( (number/max)*self.barwidth )
    remainingbar = self.barwidth - sofarbar
    # Add progress chars
    barstring += sofarbar*self.progresschar
    # If loading chars, print loading chars and go to next one (unless 100%)
    if self.loadingchars != "" and number != max:
      barstring += self.loadingchars[self.loadingcharsindex]
      self.loadingcharsindex = (self.loadingcharsindex+1) % len(self.loadingchars)
      remainingbar -= 1
    # Add remaining gap
    barstring += remainingbar*self.remainingbarchar
    # End char
    if self.startendchar:
      if len(self.startendchar) >= 2:
        barstring += self.startendchar[1]
      else:
        barstring += self.startendchar[0]

    # Post progress bar
    if self.displaypercentage:
      barstring += " %d%%" % int(number*100/max)
    if self.displaycount:
      barstring += " (%d/%d)" % (number,max)

    # Print the bar out
    sys.stdout.write(barstring)
    sys.stdout.flush()
