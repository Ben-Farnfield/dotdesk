#! /usr/bin/python

'''

'''


import getpass

from model.dot_desk_model import DotDeskModel
from util import util
from view import view


__author__ = "Ben Farnfield"
__email__ = "ben.farnfield@gmail.com"

__license__ = ""


# Install Dir's --------------------------------------------------------------

_home = "/home/" + getpass.getuser() + "/"

_icon_theme = "/usr/share/icons/hicolor/"

_global_icon_dir = _icon_theme + "{size}/apps/"
_local_icon_dir = _home + ".icons/"

_global_desk_dir = "/usr/share/applications/"
_local_desk_dir = _home + ".local/share/applications/"

_icon_to_install = None

_icon_name = None



# Install .desktop ------------------------------------------------------------

def install(args):

	program = args.i

	does_dotdesk_exist = util.make_does_dotdesk_exist(program)
	does_dotdesk_exist(_global_desk_dir) # exit if .desktop exists
	does_dotdesk_exist(_local_desk_dir)

	dotdesk = DotDeskModel(program)

	dotdesk.tooltip = view.prompt_string("Enter tooltip")

	dotdesk.terminal = view.prompt_Y_n("Terminal app?")

	yes_install_icon = view.prompt_Y_n("Install icon?")

	if yes_install_icon:
		_icon_to_install = view.prompt_path("Enter icon path",
											"Icon not found.")

		_icon_name = util.extract_file_name_from_path(_icon_to_install)
		
		if util.is_root_install(): # we need to know the icon size.
		
			dir_names = util.get_dirs(_icon_theme) # get list of icon sizes
			num_sizes = len(dir_names) # get number of icon sizes available
			
			while True:
				print "Available icon sizes:"
				view.print_dirs(_icon_theme) # print icon sizes
				select = view.prompt_select("Select 0-" + str(num_sizes-1),
											"Selection not available.",
											num_sizes)
				icon_size = dir_names[select]
				dotdesk.icon = (_global_icon_dir.format(size=icon_size) 
								+ _icon_name)
				break
		else:
			dotdesk.icon = _local_icon_dir + _icon_name

	dotdesk.exe = view.prompt_string("Enter execution command")
    
	#DEBUG
	print dotdesk.to_string()


#~ def install_icons(args):
    #~ icon_name = (PROG+"."+args.install)
    #~ for i in range(len(ICON_SIZES)):
        #~ print ("Installing "+ICON_SIZES[i]+" "+icon_name)
        #~ shutil.copyfile((WRK_DIR+"/icons/"+ICON_SIZES[i]+"/"+icon_name), 
                        #~ (ICON_INST_HOME+"/"+ICON_SIZES[i]+"/apps/"+icon_name))
#~ 
#~ 
#~ def remove_icons():
    #~ for i in range(len(ICON_SIZES)):
        #~ for j in range(len(ICON_TYPES)):
            #~ icon_path = (ICON_INST_HOME+"/"+ICON_SIZES[i]+"/apps/"
                         #~ +PROG+"."+ICON_TYPES[j])
            #~ if os.path.isfile(icon_path):
                #~ print ("Removing "+ICON_SIZES[i]+" "+PROG+"."+ICON_TYPES[j])
                #~ os.remove(icon_path)
#~ 
#~ 
#~ def install_desktop(args):
    #~ print "Installing .desktop file"
    #~ desktop = open("/usr/share/applications/"+PROG+".desktop", "w")
    #~ desktop.write(get_desktop_contents(args))
    #~ desktop.close()
#~ 
#~ 
#~ def remove_desktop():
    #~ print "Removing .desktop file"
    #~ os.remove("/usr/share/applications/"+PROG+".desktop")

# -----------------------------------------------------------------------------

#_wrk_dir = os.getcwd()

_args = util.get_args()

if _args.i:
    install(_args)
#elif _args.r:
#    print "remove"
#elif _args.g:
#    print "generate"
else:
    print "Try 'setup.py --help'"
