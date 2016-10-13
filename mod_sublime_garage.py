import functools
import BigWorld
from gui import SystemMessages


def show_system_message(message, type):
    if SystemMessages.g_instance is not None:
        # notification center is ready, push message to it
        SystemMessages.pushMessage(message, type)
    else:
        # notification center not ready, recall show_system_message with same arguments from event loop 1 second later
        BigWorld.callback(1, functools.partial(show_system_message, message, type))


show_system_message("Just do it!", SystemMessages.SM_TYPE.Warning)