import os, colorama, platform, subprocess; from colorama import Fore

softwarever = "9.11"

ostype = platform.system()
if ostype == "Linux":
    osname = "GNU/Linux"
uname = platform.uname().node
osver = platform.release()
path = subprocess.run(["pwd"], capture_output=True, text=True).stdout.strip()
packages = "soon"

arch = platform.machine()
shell = os.getenv("SHELL")
shver = subprocess.run([shell, "--version"], capture_output=True, text=True).stdout.strip()

print(f"""
        {Fore.LIGHTBLACK_EX}#####
       {Fore.LIGHTBLACK_EX}#######         {Fore.LIGHTMAGENTA_EX}MiniFetch v{softwarever}
       {Fore.LIGHTBLACK_EX}##{Fore.WHITE}O{Fore.LIGHTBLACK_EX}#{Fore.WHITE}O{Fore.LIGHTBLACK_EX}##         {Fore.LIGHTMAGENTA_EX}User: {uname}
       {Fore.LIGHTBLACK_EX}#{Fore.LIGHTYELLOW_EX}#####{Fore.LIGHTBLACK_EX}#         {Fore.LIGHTMAGENTA_EX}OS: {osname}
     {Fore.LIGHTBLACK_EX}##{Fore.WHITE}##{Fore.LIGHTYELLOW_EX}###{Fore.WHITE}##{Fore.LIGHTBLACK_EX}##       {Fore.LIGHTMAGENTA_EX}Path: {path}
    {Fore.LIGHTBLACK_EX}#{Fore.WHITE}##########{Fore.LIGHTBLACK_EX}##      {Fore.LIGHTMAGENTA_EX}Version: {osver}
   {Fore.LIGHTBLACK_EX}#{Fore.WHITE}############{Fore.LIGHTBLACK_EX}##     {Fore.LIGHTMAGENTA_EX}Packages: {packages}
   {Fore.LIGHTBLACK_EX}#{Fore.WHITE}############{Fore.LIGHTBLACK_EX}###    {Fore.LIGHTMAGENTA_EX}Arch: {arch}
  {Fore.LIGHTYELLOW_EX}##{Fore.LIGHTBLACK_EX}#{Fore.WHITE}#########{Fore.LIGHTBLACK_EX}##{Fore.LIGHTYELLOW_EX}###    {Fore.LIGHTMAGENTA_EX}Shell: {shell}
{Fore.LIGHTYELLOW_EX}######{Fore.LIGHTBLACK_EX}#{Fore.WHITE}#######{Fore.LIGHTBLACK_EX}#{Fore.LIGHTYELLOW_EX}######  {Fore.LIGHTMAGENTA_EX}Shell version: {shver}
{Fore.LIGHTYELLOW_EX}#######{Fore.LIGHTBLACK_EX}#{Fore.WHITE}#####{Fore.LIGHTBLACK_EX}#{Fore.LIGHTYELLOW_EX}#######
  {Fore.LIGHTYELLOW_EX}#####{Fore.LIGHTBLACK_EX}#######{Fore.LIGHTYELLOW_EX}##### 


""")