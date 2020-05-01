import time, sys, os

# TO USE IN YOUR CODE
#from folder.ProgressBar import ProgressBar

class ProgressBar:
  def __init__(self,
              pretext="", # Test to print before the bar
              progresschar="-", # Character to show progress
              loadingchars=r"\|/", # Last character of bar moving as bar loads (moves even if no progress)
              startendchar="[]", # Characters going around the bar
              barwidth=int(os.get_terminal_size().columns/2), # Length of the bar in characters (does not include what's around the bar)
              displaypercentage=False, # Show percentage as well or not
              displaycount=False # Show count as well or not
              ):
    self.pretext = str(pretext)
    self.progresschar = str(progresschar)
    self.loadingchars = loadingchars
    self.startendchar = str(startendchar)
    self.barwidth = int(barwidth)
    self.displaypercentage = displaypercentage
    self.displaycount = displaycount

    # loadingchars ideas
    # characters = "-/|\"
    # characters = ["-_="]

    # Private
    self.loadingcharsindex = 0
    self.firstprint = True
  

  # Role : print the progress bar as an independent thread
  # Arguments:
  #   number: multiprocessing.Value
  #   total: value to reach
  #   updateperiod: refresh period of progress bar in seconds
  # Example:
  #   number = multiprocessing.Value("i", 0)
  #   total = 30
  #   progressbar = ProgressBar()
  #-> multiprocessing.Process(target=progressbar.inThread, args=(number,total,0.1))
  #   for i in range(0,total)
  #     number.value = i
  def inThread(self, number, total, updateperiod=0.1):
    while(number.value != total):
      self.print(number.value,total)
      time.sleep(float(updateperiod))
    self.print(total,total)


  # Role : print the progress bar
  # Arguments:
  #   number: progress value
  #   total: maximum value
  # Example:
  #   total = 30
  #   progressbar = ProgressBar()
  #   for i in range(0,total):
  #->   progressbar.print(i, total)
  def print(self,number,total):
    barstring = ""

    # No carriage return on first print
    if not self.firstprint:
      barstring += "\r"
    self.firstprint = False

    # Pre progress bar
    if self.pretext:
      barstring += self.pretext

    # Progress bar
    #Start char
    if self.startendchar:
      barstring += self.startendchar[0]
    #Current state of affairs
    sofarbar = int( (number/total)*self.barwidth )
    remainingbar = self.barwidth - sofarbar
    #Add progress chars
    barstring += sofarbar*self.progresschar
    #If loading chars, print loading chars and go to next one (unless 100%)
    if self.loadingchars != "" and number != total:
      barstring += self.loadingchars[self.loadingcharsindex]
      self.loadingcharsindex = (self.loadingcharsindex+1) % len(self.loadingchars)
      remainingbar -= 1
    #Add remaining gap
    barstring += remainingbar*" "
    #End char
    if self.startendchar:
      if len(self.startendchar) >= 2:
        barstring += self.startendchar[1]
      else:
        barstring += self.startendchar[0]

    # Post progress bar
    if self.displaypercentage:
      barstring += " %d%%" % int(number*100/total)
    if self.displaycount:
      barstring += " (%d/%d)" % (number,total)

    # Print the bar out
    sys.stdout.write(barstring)
    sys.stdout.flush()