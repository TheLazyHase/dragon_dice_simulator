dragon_dice_simulator
=====================

Something about dragons. And dices.

For requirement, I advice to use virtualenv:

sudo apt-get install virtualenv
virtualenv .
. bin/activate
pip install pyramid

* comment may often be in engrish.
* the code have not sanity-checked yet, so it may have some cosmic horror lurking in some classes
* roll.py is the file in which I dump my tests to se if everything work, it's not something needed for the thing to work.
* the get_result method of the army class is certainly to be cleaned up and reworked
* the fly SAI work, be there seem to be way too much code to do something so simple.
* some timings and rules are a bit off, mainly dragon roll is actually treated as an action roll (and trigger cantrip)
* only frostwing units and SAI are in the data. Other are not planned to be added until I add a db layer.

Next in line :
* add pyramid as web framework, because it will be significantly easier to both code and use than command-line commands
* use sqlalchemy + some db (postgresql, mysql ?) to persist information
* make a virtualenv to make dependancy works without hurdles
