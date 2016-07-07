# user_performance_monitor AKA scrncap
this small cross-platform python script gets frequent and random screen shots in a configured frequency. it can be used to monitor work behavior on an end user machine.
it is tested on ubutu linux and windows 10 , however it should work on other versions of these operating systems as well
default frequency on which it take screen shots is 10 min
dependencies:
1. install Python 2.7 https://www.python.org/downloads/ 
  dont forget to add python2.7 to your path ENV variable on windows
2. install pyscreenshot   "sudo pip install pyscreenshot" on linux or  "pip install pyscreenshot" on windows
3. install pillow         "sudo pip install pillow" on linux or "pip install pillow" on windows

to run the script 
python scrncap

road map:
1. making randomization of screenshots configurable
2. ability to save screen shots on a remote machine via (S)FTP and similar protocols
3.ability to remotly configure and manage the script
4.making the app window based instead of command line based
5.building another APP for remote mgmt and config of this script and continous monitoring of  screenshots

any comment/question is welcomed at hgee83@gmail.com
