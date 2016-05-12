#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004 All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
"""
This module contains the base class for pathos servers, and describes
the pathos server interface.  If a third-party RPC server is selected,
such as 'parallel python' (i.e. 'pp') or 'RPyC', direct calls to the
third-party interface are currently used.

"""
__all__ = ['Server']

class Server(object):
    """
Server base class for pathos servers for parallel and distributed computing.
    """

    def selector(self):
        """get the selector"""
        return self._selector


    def deactivate(self):
        """turn off the selector"""
        self._selector.state = False
        return

    
    def activate(self, onTimeout=None, selector=None):
        """configure the selector and install the timeout callback"""

        if selector is None:
            import pyre.ipc
            selector = pyre.ipc.selector()

        if onTimeout is not None:
            selector.notifyWhenIdle(onTimeout)

        self._selector = selector

        return


    def serve(self, timeout):
        """begin serving, and set the timeout"""
        self._selector.watch(timeout)
        return


    def __init__(self):
        """
Takes no initial input.
        """
        self._selector = None
        return


# End of file
