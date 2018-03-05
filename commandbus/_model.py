from abc import abstractmethod, ABC


class Command:
    pass


class CommandHandler(ABC):
    @abstractmethod
    def handle(self, cmd: Command):
        pass


class CommandBus:
    def __init__(self):
        self._commands = {}
        self._executing = False

    def subscribe(self, cmd: type, handler: CommandHandler):
        if cmd in self._commands:
            from commandbus import CommandAlreadyExistException
            raise CommandAlreadyExistException
        self._commands[cmd] = handler

    def publish(self, cmd: Command):
        if cmd.__class__ not in self._commands:
            from commandbus import CommandHandlerDoesNotExistException
            raise CommandHandlerDoesNotExistException()
        if self._executing:
            from commandbus import CommandExecutionAlreadyInProgressException
            raise CommandExecutionAlreadyInProgressException()
        self._executing = True
        try:
            self._commands[cmd.__class__].handle(cmd)
        finally:
            self._executing = False
