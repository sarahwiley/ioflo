"""globaling.py module with global constang

"""
print "Module %s" % __name__

import math
import re


#debugging support
#debug = True
debug = False

#Globals
#Constant Definitions
TIME1970 = 2208988800L #offset secs between SNTP epoch=1900 & unix epoch=1970
TWOPI = 2.0 * math.pi # two times pi
DEGTORAD = math.pi / 180.0 # r = DEGTORAD * d
RADTODEG = 180.0 / math.pi # d = RADTODEG * r

#Task generator control values
STOP = 0
START = 1
RUN = 2
ABORT = 3
READY =  4
ControlNames = { STOP : 'Stop', START : 'Start', RUN : 'Run', ABORT : 'Abort', READY : 'Ready',}

#Task generator operational status
STOPPED = STOP
STARTED = START
RUNNING = RUN
ABORTED = ABORT
READIED = READY
StatusNames = { STOPPED : 'Stopped', STARTED : 'Started', RUNNING : 'Running', ABORTED : 'Aborted', READIED : 'Readied', }
StatusValues = { 'Stopped' : STOPPED, 'Started' :  STARTED, 'Running' : RUNNING, 'Aborted' : ABORTED, 'Readied' : READIED,}

#log rule values
NEVER = 0
ONCE = 1
ALWAYS = 2
UPDATE = 3
CHANGE = 4
LogRuleNames = {NEVER : 'Never', ONCE : 'Once', ALWAYS : 'Always', 
                UPDATE : 'Update', CHANGE : 'Change'}
LogRuleValues = {'Never' : NEVER, 'Once' : ONCE,  'Always' : ALWAYS, 
                 'Update' : UPDATE, 'Change' : CHANGE}

#Task schedule context
INACTIVE = 0
ACTIVE = 1
AUX = 2
SLAVE = 3
ScheduleNames = { INACTIVE : 'inactive', ACTIVE : 'active', AUX : 'aux', SLAVE : 'slave'}
ScheduleValues = { 'inactive': INACTIVE , 'active':  ACTIVE, 'aux': AUX, 'slave': SLAVE}

#Task ordering
MID = 0
FRONT = 1
BACK = 2

OrderNames = { MID : 'mid', FRONT : 'front', BACK : 'back'}
OrderValues = { 'mid': MID , 'front':  FRONT, 'back': BACK}

#Frame action contexts
NATIVE = 0
ENTER = 1
RECUR = 2
PRECUR = 3
EXIT = 4
RENTER = 5
REXIT = 6
BENTER = 7
PREAUX = 8

ActionContextValues = { 'native': NATIVE , 'enter':  ENTER, 'recur': RECUR,
                        'precur': PRECUR, 'exit': EXIT, 'renter': RENTER, 'rexit': REXIT,
                        'benter': BENTER, 'preaux': PREAUX}
ActionContextNames = { NATIVE : 'native', ENTER : 'enter', RECUR : 'recur', 
                       PRECUR : 'precur', EXIT : 'exit', RENTER : 'renter', REXIT : 'rexit',
                       BENTER : 'benter', PREAUX : 'preaux'}


#Precompile re match objects

#regular expression objects to quickly determine if string is valid python identifier
#Usage: REO_Identifier.match('Hello') returns match object if match otherwise None
REO_Identifier = re.compile(r'^[a-zA-Z_]\w*$') #valid python identifier
REO_IdentPub = re.compile(r'^[a-zA-Z]\w*$') #valid python public identifier ie no leading underscore

# regex objects to determine if string is valid store path
# to use 
#if REO_Path.match(s):
#  then s is valid path

REO_Path = re.compile(r'^([a-zA-Z_]\w*)+([.][a-zA-Z_]\w*)*$|^([.][a-zA-Z_]\w*)+$')
REO_RelPath = re.compile(r'^([a-zA-Z_]\w*)+([.][a-zA-Z_]\w*)*$')
REO_DotPath = re.compile(r'^([.][a-zA-Z_]\w*)+$')
REO_PathDotPath = re.compile(r'^([a-zA-Z_]\w*)+([.][a-zA-Z_]\w*)+$|^([.][a-zA-Z_]\w*)+$')

#regex object to split hafscript command line
REO_Chunks = re.compile(r'#.*|[^ "]+|"[^"]*"') 
# Usage
# chunks = REO_Chunks.findall(s)

# to match each part
REO_Quoted = re.compile(r'^"[^"]*"$')  
REO_Comment = re.compile(r'^#.*$')
REO_Plain = re.compile(r'^[^ "]+$')
#Usage
# if REO_Quoted.match(s):
#    s.strip('"')

#regex object determine if lat or lon is in human readable form
#REO_LATLONPOS = re.compile(r'^([0-9]+)[N,E,n,e]([0-9]+\.[0-9]+)$') 
REO_LatLonNE = re.compile(r'^(\d+)[N,E,n,e](\d+\.\d+)$') 
REO_LatLonSW = re.compile(r'^(\d+)[S,W,s,w](\d+\.\d+)$') 
#Usage
# ll = REO_LatLonNE.findall(s) #returns list of tuples of groups [(deg,min)]
# if ll:
#   deg = float(ll[0][0])
#   min = float(ll[0][1])
#   fracdeg = deg + min/60.0

def Test():
    """Module Common self test

    """
    global debug

    oldDebug = debug
    debug = True #turn on debug during tes


    debug = oldDebug #restore debug value


if __name__ == "__main__":
    Test()

