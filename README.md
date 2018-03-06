<h2 align="center"><code>commandbus</code></h2>
<p align="center">
<a href="https://badge.fury.io/py/commandbus"><img src="https://badge.fury.io/py/commandbus.svg" alt="PyPI version" height="18"></a>
</p>
## 📜 About
Command bus is a pattern from CQRS. In this pattern we have three components:

* `Command`: represents the desired action to be done, like `RegisterUserCommand`.
* `CommandHandler`: retrieves the data from the command and executes all the actions to accomplish the command 
objective. In the previous case creates a new user and saves it do database. 
* `CommandBus`: routes the command to the handler 

## ⚒️ Installation
Installation is so easy, you only need to execute
```
pip install commandbus
```

## 🚀 Using commandbus
Using command is as easy as type
```python3
from commandbus import Command, CommandHandler, CommandBus

class SomeCommand(Command):
    pass

class SomeCommandHandler(CommandHandler):
    def __init__(self):
        self.called = False

    def handle(self, cmd: Command):
        self.called = True
        
bus = CommandBus()
handler = SomeCommandHandler()
bus.subscribe(SomeCommand, handler)
assert not handler.called
bus.publish(SomeCommand())
assert handler.called
```


## 🚩 License
The code is available under the MIT license.
