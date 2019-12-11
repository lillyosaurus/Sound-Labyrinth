'''import pyttsx3
def onWord(name, location, length):
   print ('word', name, location, length)
   if location > 10:
      engine.stop()

engine = pyttsx3.init()
engine.setProperty('rate', 100)
engine.connect('started-word', onWord)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''

'''
import pyttsx3
def onStart(name):
   print ('starting', name)
def onWord(name, location, length):
   print ('word', name, location, length)
def onEnd(name, completed):
   print ('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''

"""
import pyttsx3
import logging
from time import sleep
from multiprocessing.dummy import Process as Thread
#from threading import Thread

logger = logging.getLogger(__name__)

class VoiceBox(object):
    def __init__(self):
        self.t = None
        self._running = False
        self.engine = None

    def _processSpeech(self, text):
        self.engine = pyttsx3.init()
        self.engine.say(str(text))
        self.engine.startLoop(False)
        while self._running:
            self.engine.iterate()
        logger.debug('Thread loop stopped')

    def say(self, text, noInter=2):
        # check if thread is running
        if self.t and self._running:
            logger.debug('Interupting...')
            # stop it if it is
            self.stop()
        # iterate speech in a thread
        logger.debug('Talking: %s', text)
        self.t = Thread(target=self._processSpeech, args=(text,))
        self._running = True
        self.t.daemon = True
        self.t.start()
        # give the thread some space
        # without this sleep and repeatitive calls to 'say'
        # the engine may not close properly and errors will start showing up
        sleep(noInter)

    def stop(self):
        self._running = False
        try:
            self.engine.endLoop()
            logger.debug('Voice loop stopped')
        except:
            pass
        try:
            self.t.join()
            logger.debug('Joined Voice thread')
        except Exception as e:
            logger.exception(e)



if __name__ == '__main__':
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)
    text = '''
    Hobsbawm joined the Communist Party in 1936 and stayed in it for about fifty years. Not only did the cause to which he had devoted his life expire in infamy but the rubbish that it had promised to sweep from the stage-ethnic and national chauvinism-would, in time, make a new bid for legitimacy.
    '''
    text2 = '''
    pepe hands
    '''
    v = VoiceBox()
    v.say(text, 10)
    v.say(text2)
    # I would like to have v.say() know when it is finished talking
    # kill the voice engine and join the talking thread.
    #v.stop()
"""

import keyboard
import pyttsx3

def init():
    print("init")
    def start(text):
        engine = pyttsx3.init()
        #more code here but its just setting the volume and speech rate
        engine.say(text,"txt")
        engine.runAndWait()

    def onWord(name, location, length):
        print ('word', name, location, length)
        if keyboard.is_pressed("esc"):
            engine.stop()

            engine.connect('started-word', onWord)

    def action():
        #win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        #win32clipboard.CloseClipboard()
        start(data)

        keyboard.add_hotkey("ctrl+alt", lambda: action())

    init()

'''
import keyboard
import win32clipboard
import pyttsx3

def init():
    print("init")
    def start(text):
        engine = pyttsx3.init()
        #more code here but its just setting the volume and speech rate
        engine.say(text,"txt")
        engine.runAndWait()

    def action():
      win32clipboard.OpenClipboard()
      data = win32clipboard.GetClipboardData()
      win32clipboard.CloseClipboard()
      start(data)

    keyboard.add_hotkey("ctrl+alt", lambda: action())

init()
'''
