#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2019 by sailoog <https://github.com/sailoog/openplotter>
#                     e-sailing <https://github.com/e-sailing/openplotter>
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.
import subprocess

class Ports:
	def __init__(self,conf):
		self.usedPorts=[]
		out = subprocess.check_output(['systemctl', 'is-active', 'vncserver-x11-serviced.service']).decode('utf-8')
		if not 'inactive' in out: 
			self.usedPorts=[{'description':_('VNC Remote Desktop'), 'type':'TCP', 'address':'localhost', 'port':'5900', 'direction':'out'}]