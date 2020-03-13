#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

from threading import Thread
import pexpect

class Client(Thread):
    """docstring for Client."""

    def __init__(self, host:str, port:int, protocol="nc", debug=True):
        Thread.__init__(self)
        self.daemon = True
        #=[End of thread conf]====================
        self._debug_    = debug
        self.host       = str(host)
        self.port       = max(min(65535, int(port)), 0)
        self.protocol   = protocol
        self.conn       = None
        self.connected  = False
        self.running    = True
        self.buffer     = ""
        self.msgs = {
            "co_lost"    : "***** Connection Lost *****",
            "co_timeout" : "*** Connection Timed Out ***"
        }

    def debug(self, message):
        if self._debug_ :
            print("\x1b[1m[\x1b[93mdebug\x1b[0m\x1b[1m]\x1b[0m \x1b[94m"+__name__+"\x1b[0m : "+message)
        return None

    def connect(self):
        """Documentation for connect"""
        self.debug("Client.connect()")
        try:
            self.debug(""+self.protocol+" "+self.host+" "+str(self.port))
            self.conn = pexpect.spawn(self.protocol+" "+self.host+" "+str(self.port))
            self.connected = True
        except Exception as e:
            self.connected = False
        self.debug("connected : "+str(self.connected))
        return self.connected

    def run(self):
        self.debug("Client.run()")
        self.running = self.connect()
        while self.running:
            if self.connected == True:
                try:
                    self.conn.expect('.')
                    self.buffer += self.conn.after.decode("ISO-8859-1")
                except pexpect.EOF:
                    self.debug("\x1b[1;91mException :\x1b[0m EOF")
                    self.running = False
                    self.buffer += "\n"+self.msgs["co_lost"]
                except pexpect.TIMEOUT:
                    self.debug("\x1b[1;91mException :\x1b[0m TIMEOUT")
                    self.running = False
                    self.buffer += "\n"+self.msgs["co_timeout"]
        self.debug("Client stopped.")

    def send(self, text:str):
        """Documentation for send"""
        self.conn.sendline(text+"\r")
        return

    def read(self):
        """Documentation for read"""
        copy = self.buffer[:]
        self.buffer = ""
        return copy

    def reconnect(self):
        """Documentation for stop"""
        self.conn       = None
        self.connected  = False
        self.running    = True
        self.buffer     = ""
        self.run()

    def stop(self):
        """Documentation for stop"""
        self.running = False

# *----------------------------------Get Set---------------------------------- *

    def get_host(self):
        return self.host

    def set_host(self, host):
        if type(self.host) == str:
            self.host = host
        return self

    def get_port(self):
        return self.port

    def set_port(self, port):
        if type(self.port) == tint:
            self.port = port
        return self
