import time, sys

class ProgressBar:
  def __init__(self,
              pretext="",
              progresschar="-",
              loadingchars=r"\-/|",
              startendchar="[]",
              barwidth=int(100/3),
              displaypercentage=False,
              displaycount=False
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
  
  # Function to link to a thread
  def inThread(self, number, total, updateperiod=0.1):
    while(progressnumber.value != total):
      self.print(False,number.value,total)
      time.sleep(float(updateperiod))
    self.print(False,total,total)

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
    barstring += self.startendchar[0]
    #Current state of affairs
    sofarbar = int( (number/total)*self.barwidth )
    remainingbar = self.barwidth - sofarbar
    #If loading chars, make sure there's space to print it
    if self.loadingchars != "" and sofarbar > 0:
      sofarbar -= 1
    #Add progress chars
    barstring += sofarbar*self.progresschar
    #If loading chars, print loading chars and go to next one
    if self.loadingchars != "":
      barstring += self.loadingchars[self.loadingcharsindex])
      self.loadingcharsindex = (self.loadingcharsindex+1) % len(self.loadingchars)
    #Add remaining gap 
    barstring += remainingbar*" "
    #End char
    barstring += self.startendchar[0]

    # Post progress bar
    if self.displaypercentage:
      barstring += " %d%%" % int(number*100/total)
    if self.displaycount:
      barstring += " (%d/%d)" % (number,total)

    # Print the bar out
    sys.stdout.write(barstring)
    sys.stdout.flush()