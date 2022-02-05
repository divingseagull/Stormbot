from nextcord.ext import commands
import nextcord
import os
import subprocess
import psutil

server64Path = None

server = subprocess.Popen([])
server.kill()