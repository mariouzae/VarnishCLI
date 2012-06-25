VarnishCLI
==========

Varnish Command-Line Interface - Version 0.1 BETA

This software was created to execute commands for more than one Varnish's servers. For example, if you 
have two Varnish's server and wish invalidate an one object by Varnishadm, with this software you can execute 
one command to execute in several Varnish Server's.

For this work, you should configure the "config.cfg" file with descrive below:

" config.cfg
[node1]
host = foo.com.br
username= varnishadm
password = /root/.ssh/id_rsa.pub

To inicialize the console:

./varnishadm.py -c config.cfg