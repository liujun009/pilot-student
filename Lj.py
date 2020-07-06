from time import sleep
from termcolor import colored
from simpleeval import simple_eval
from random import choice

class Bot:

    wait = 1

    def __init__(self, runtype='once'):
        self.runtype = runtype
        self.q = ''
        self.a = ''

    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'red')

    def _run_once(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))

    def _run_looped(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        while True:
            self.a = input()
            if self.a.lower() in ['q','x','quit','exit']:
                break
            sleep(Bot.wait)
            print(self._format(self._think(self.a)))

    def run(self):
        if self.runtype == 'once':
            self._run_once()
        elif self.runtype == 'looped':
            self._run_looped()


class HelloBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "Hi,what is your name?"
        
    def _think(self, s):
        return f"Hello {s}"

class GreetingBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "How are you today?"
        
    def _think(self, s):
        if "good" in s.lower() or "fine" in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that"

import random

class FavoriteColorBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "What's your favorite color?"
        
    def _think(self, s):
        colors = ['red', 'orange','yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"

class CalcBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "Though recent upgrade I can calculation now.Input some arithmetic expression to try:"

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"


class Shi:
    
    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []
        
    def add(self, bot):
        self.bots.append(bot)
        
    def _prompt(self,s):
        print(s)
        print()
        
    def run(self):
        self._prompt("This is Shi dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()

shi = Shi(1)
shi.add(HelloBot())
shi.add(GreetingBot())
shi.add(FavoriteColorBot())
shi.add(CalcBot('looped'))
shi.run()                                                