import pytest

from commandbus import Command, CommandHandler, CommandBus, CommandExecutionAlreadyInProgressException, \
    CommandAlreadyExistException, CommandHandlerDoesNotExistException


class SomeCommand(Command):
    pass


class SomeCommandHandler(CommandHandler):
    def __init__(self):
        self.called = False

    def handle(self, cmd: Command):
        self.called = True


class SomeCommandCallsAnotherCommandHandler(CommandHandler):
    def __init__(self, bus):
        self._bus = bus

    def handle(self, cmd: Command):
        self._bus.publish(SomeCommand())


@pytest.fixture
def bus():
    return CommandBus()


def test_handle_command(bus):
    handler = SomeCommandHandler()
    bus.subscribe(SomeCommand, handler)
    assert not handler.called
    bus.publish(SomeCommand())
    assert handler.called


def test_should_throw_exception_when_call_another_command_inside_a_command(bus):
    handler = SomeCommandCallsAnotherCommandHandler(bus)
    bus.subscribe(SomeCommand, handler)
    with pytest.raises(CommandExecutionAlreadyInProgressException):
        bus.publish(SomeCommand())


def test_should_throw_command_already_exists_exception(bus):
    handler = SomeCommandHandler()
    bus.subscribe(SomeCommand, handler)
    with pytest.raises(CommandAlreadyExistException):
        bus.subscribe(SomeCommand, handler)


def test_should_throw_command_does_not_exist_exception(bus):
    with pytest.raises(CommandHandlerDoesNotExistException):
        bus.publish(SomeCommand)
