from sys import stdout, stdin
from time import sleep

class fg:

  """
  fg.<color>
  please type a valid color
  black, red, green, yellow, blue, magenta, cyan, white, brightBlack, brightRed, brightGreen, brightYellow, brightBlue, brightMagenta, brightCyan, brightWhite
  """

  black = "\u001b[30m"
  red = "\u001b[31m"
  green = "\u001b[32m"
  yellow = "\u001b[33m"
  blue = "\u001b[34m"
  magenta = "\u001b[35m"
  cyan = "\u001b[36m"
  white = "\u001b[37m"
  brightBlack = "\u001b[90m"
  brightRed = "\u001b[91m"
  brightGreen = "\u001b[92m"
  brightYellow = "\u001b[93m"
  brightBlue = "\u001b[94m"
  brightMagenta = "\u001b[95m"
  brightCyan = "\u001b[96m"
  brightWhite = "\u001b[97m"

  def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"
  """
  rgb(<num>,<num>,<num>)
  takes in an RGB value and sets the foreground color to the rgb value.
  """

class bg:
  """
  bg.<color>
  please type a valid color
  black, red, green, yellow, blue, magenta, cyan, white, brightBlack, brightRed, brightGreen, brightYellow, brightBlue, brightMagenta, brightCyan, brightWhite
  """
  black = "\u001b[40m"
  red = "\u001b[41m"
  green = "\u001b[42m"
  yellow = "\u001b[43m"
  blue = "\u001b[44m"
  magenta = "\u001b[45m"
  cyan = "\u001b[46m"
  white = "\u001b[47m"
  brightBlack = "\u001b[100m"
  brightRed = "\u001b[101m"
  brightGreen = "\u001b[102m"
  brightYellow = "\u001b[103m"
  brightBlue = "\u001b[104m"
  brightMagenta = "\u001b[105m"
  brightCyan = "\u001b[106m"
  brightWhite = "\u001b[107m"

  def rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"
  """
  rgb(<num>,<num>,<num>)
  takes in an RGB value and sets the background color to the rgb value.
  """
class util:
  
  reset = "\u001b[0m"

  """ 
  Resets the color 
  """
  
  bold = "\u001b[1m"

  """ 
  Makes the text bold 
  """
  
  underline = "\u001b[4m"

  """ 
  Makes the text underline 
  """
  
  reverse = "\u001b[7m"

  """ 
  Reverses the text
  """

  clear = "\u001b[2J"
  clearline = "\u001b[2K"

  up = "\u001b[1A"
  down = "\u001b[1B"
  right = "\u001b[1C"
  left = "\u001b[1D"
  
  nextline = "\u001b[1E"
  prevline = "\u001b[1F"

  top = "\u001b[0;0H"

  def to(x, y):
    return f"\u001b[{y};{x}H"

  def write(text="\n"):
    stdout.write(text)
    stdout.flush()

  def writew(text="\n", wait=0.5):
    for char in text:
      stdout.write(char)
      stdout.flush()
      sleep(wait)

  def read(begin=""):
    text = ""

    stdout.write(begin)
    stdout.flush()

    while True:
      char = ord(stdin.read(1))
      
      if char == 3: return
      elif char in (10, 13): return text
      else: text += chr(char)

  def readw(begin="", wait=0.5):
    text = ""

    for char in begin:
      stdout.write(char)
      stdout.flush()
      sleep(wait)

    while True:
      char = ord(stdin.read(1))
      
      if char == 3: return
      elif char in (10, 13): return text
      else: text += chr(char)
