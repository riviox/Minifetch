import colorama
from colorama import *
import os
import platform
import subprocess

softwarever = "9.11"

ostype = os.sys.platform
if ostype == "linux":
    osname = "GNU/Linux"
uname = os.getlogin()
osver = platform.release()
path = os.getcwd()
packages = "soon"
archp = platform.architecture()
if archp == "('64bit', 'ELF')":
    arch = "64bit"
else:
    arch = "32bit"


shell = "C:\Windows\System32\cmd.exe"
print(f"""
        {Fore.LIGHTBLACK_EX}#####            
       {Fore.LIGHTBLACK_EX}#######         {Fore.LIGHTMAGENTA_EX}MiniFetch v{softwarever}
       {Fore.LIGHTBLACK_EX}##{Fore.WHITE}O{Fore.LIGHTBLACK_EX}#{Fore.WHITE}O{Fore.LIGHTBLACK_EX}##         {Fore.LIGHTMAGENTA_EX}User: {uname}
       {Fore.LIGHTBLACK_EX}#{Fore.LIGHTYELLOW_EX}#####{Fore.LIGHTBLACK_EX}#         {Fore.LIGHTMAGENTA_EX}OS: {osname}
     {Fore.LIGHTBLACK_EX}##{Fore.WHITE}##{Fore.LIGHTYELLOW_EX}###{Fore.WHITE}##{Fore.LIGHTBLACK_EX}##       {Fore.LIGHTMAGENTA_EX}Path: {path}
    {Fore.LIGHTBLACK_EX}#{Fore.WHITE}##########{Fore.LIGHTBLACK_EX}##      {Fore.LIGHTMAGENTA_EX}Version: {osver}
   {Fore.LIGHTBLACK_EX}#{Fore.WHITE}############{Fore.LIGHTBLACK_EX}##     {Fore.LIGHTMAGENTA_EX}Arch: {arch}
   {Fore.LIGHTBLACK_EX}#{Fore.WHITE}############{Fore.LIGHTBLACK_EX}###    {Fore.LIGHTMAGENTA_EX}Shell: {shell}
  {Fore.LIGHTYELLOW_EX}##{Fore.LIGHTBLACK_EX}#{Fore.WHITE}#########{Fore.LIGHTBLACK_EX}##{Fore.LIGHTYELLOW_EX}###    {Fore.LIGHTMAGENTA_EX}
{Fore.LIGHTYELLOW_EX}######{Fore.LIGHTBLACK_EX}#{Fore.WHITE}#######{Fore.LIGHTBLACK_EX}#{Fore.LIGHTYELLOW_EX}######  {Fore.LIGHTMAGENTA_EX}
{Fore.LIGHTYELLOW_EX}#######{Fore.LIGHTBLACK_EX}#{Fore.WHITE}#####{Fore.LIGHTBLACK_EX}#{Fore.LIGHTYELLOW_EX}#######   
  {Fore.LIGHTYELLOW_EX}#####{Fore.LIGHTBLACK_EX}#######{Fore.LIGHTYELLOW_EX}##### 


""")