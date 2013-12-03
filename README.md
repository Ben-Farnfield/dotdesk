# dotdesk

dotdesk is a simple Python utility written to create and install .desktop files along with their companion .png or .svg icons.

#### Install
Open a terminal within the directory you wish to install dotdesk and run:
```
git clone https://github.com/Ben-Farnfield/dotdesk.git
cd dotdesk
sudo ./install.py -i
```

#### Remove
Open a terminal within you dotdesk install directory and run:
```
sudo ./install.py -r
```

## dotdesk usage

#### Install .desktop
Open a terminal and run:
```
sudo dotdesk -i [program name]
```

#### Remove .desktop
*note: you should only remove .desktop files which have been installed using dotdesk*
```
sudo dotdesk -r [program name]
```

## Interface

dotdesk provides a simple terminal interface for inputting relevant data.

```
user@comp: sudo dotdesk -i eclipse

> Terminal app? y/n: n

> Enter tooltip: Java IDE

> Enter execution command: /opt/eclipse/eclipse

Select a category:

 [0]...AudioVideo
 [1]........Audio
 [2]........Video
 [3]..Development
 [4]....Education
 [5].........Game
 [6].....Graphics
 [7]......Network
 [8].......Office
 [9]......Science
[10].....Settings
[11].......System
[12]......Utility

> Make a selection: 3

> Install an icon? y/n: y

> Enter full path to icon: /home/user/Downloads/eclipse.svg

Select icon size:

 [0]........48x48
 [1]........64x64
 [2].....scalable

> Make a selection: 2

------------------------------

eclipse.desktop installed!
eclipse.svg installed!
Bye!

------------------------------

```

## Me

If you have further questions you can reach me at:
ben.farnfield@gmail.com
