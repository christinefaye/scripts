#!/usr/bin/python

import socket
from cmConnect import cConnect
'''
Module to describe host properties

'''

#TODO:
 # verify ip


class cHost:
  ''' Remote host class '''
  # user	: string for host username
  # passwd	: string for host password
  # ip		: string for host aipv4 address
  # url		: string for host uniform resource locator
  def __init__(self,user,passwd,ip=None,url=None):
    self.usr = user		# Host username
    self.pwd = passwd		# Host password
    self.ip = ip		# Host ip address
    self.url = url.strip()	# Host url
    self.cnxn = None		# a cConnect object
    if not self.ip:
      self.urlToIp()
      if self.validateIPv4():
        assert self.ip
    assert self.usr and self.pwd and self.ip

  def urlToIp(self):
    ''' Convert URL to IP'''
    self.ip=socket.gethostbyname(self.url)

  def validateIPv4(self):
    ''' Check if IPv4 address is valid '''
    if socket.inet_aton(self.ip):
      return True
    return None

  def createCnxn(self):
    ''' Create a connection '''
    self.cnxn = cConnect(self.usr,self.pwd,self.ip)
    self.cnxn.ssh()

#----------END CLASS-------------#





