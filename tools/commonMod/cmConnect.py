#!/usr/bin/python

#TODO:

'''
Module to connect to a host

'''

import paramiko

class cConnect:
  ''' Connection to host class '''
  # user	: string for host username
  # passwd	: string for host password
  # ip		: string for host ip
  def __init__(self,user,passwd,ip):
    self.usr = user		# Host username
    self.pwd = passwd		# Host password
    self.ip = ip		# Host ip address
    self.ssh = None		# Paramiko SSH object

  def ssh(self):
    ''' SSH connection to host '''
    self.ssh = paramiko.SSHClient()
    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    self.ssh.connect(self.ip,username=self.usr,password=self.pwd)
    stdin,stdout,sterr=self.ssh.exec_command("uptime")
    print type(stdin)
    print stdout.readlines()

    
#----------END CLASS-------------#





