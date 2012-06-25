#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  varnishadm.py
#  
#  Copyright 2012 mgusilva <mgusilva@fcl.com.br>
#  Company: Fundacao Casper Libero
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
import sys
import os
import ConfigParser
import paramiko

def execCMD(host, username, password, cmd):
 # Show where the command will be executed
 print "\n############################################"
 print "Command executed in the " + host 
 print "############################################\n"
 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
 # Receives params of the user, pass and host
 ssh.connect(host, username=username, key_filename=password)
 # Execute It !
 ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
 print "output", ssh_stdout.read() #Reading output of the executed command
 error = ssh_stderr.read()
 # Reading the error stream of the executed command
 print "error", error, len(error)
 ssh.close()

# Configuration file Parsing
def readConfig(file, cmd):
 Config = ConfigParser.ConfigParser()
 Config.read(file)
 sections = Config.sections()
 
 for section in sections:
  for values in  Config.items(section):
   if values[0] == "host":
    host = values[1]
    print host
   else:
    if values[0] == "username":
     username = values[1]
    else:
     if values[0] == "password":
      password = values[1]

  # Call function to execute this commands
  execCMD(host, username, password, cmd)

# Major Console Line Interface
def main():
 # Verify args passed by users.
 for arg in range(len(sys.argv)):
  # Define what is the configuration file.
  if sys.argv[arg] == "--config" or sys.argv[arg] == "-c":
   file = sys.argv[arg+1]
  # Anothers possibles parameters.
  elif sys.argv[arg] == "--help":
   helper = '''Usage: ./varnishadm [OPTIONS]... [FILE]...
Varnish CLI - Command-Line Interface (Built: 2012/06/24 Version: 0.1 BETA )
Options\n
 -c, --config	Set alternative configuration file, default is ./config.cfg\n'''
   print helper ; sys.exit()
 
 # Try locate the config file, if you can't find it, dies! 
 try:
  open(file) 
 except:
  print "Configuration file can not be found, you can try --config or --help"
  sys.exit()
 
 # Start Command-Line Interface.
 while(1):
  # Reinicialize the flag
  cmdNULL = "0"
  # Commands entries users
  var = raw_input("varnishCLI> ")
  # Verify users entries.
  if var == "":
   cmdNULL = "1"
  elif var == "quit":
   print "Bye."
   sys.exit()
  elif var == "?":
   print "Use the Varnish console commands."
   cmdNULL = "1"
  # Run the command received by user.
  elif cmdNULL != "1":
   cmd = "varnishadm " + var
   readConfig(file, cmd)
  else:
   print "error"
   

# Init 
if __name__ == '__main__':
 main()
