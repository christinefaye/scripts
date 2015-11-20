#!/usr/bin/python

class cRemoteHost:
  # Remote host class
  def __init__(self,user,passwd,ip=None,url=None):
    self.usr = user
    self.pwd = passwd
    self.ip = ip
    self.url = url

