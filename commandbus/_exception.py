class CommandBusException(Exception):
    pass


class CommandAlreadyExistException(CommandBusException):
    pass


class CommandHandlerDoesNotExistException(CommandBusException):
    pass


class CommandExecutionAlreadyInProgressException(CommandBusException):
    pass
