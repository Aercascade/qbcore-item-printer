QBcore-Item-Printer does exactly what is says.
A simple Python script to empower users in making items more efficiently. Decided on because creating 3 unique .txt files everytime would be incredibly time consuming.
Hopefully this helps some of you create projects a little easier.
See some of the example outputs in the .txt files provided.


This python script will show you a console to take you through each entry.
['name'] = what is used for spawning. It should not have a space in the name use '_' or '-' instead.

['label'] = what is used ingame, so what the player will see.

['weight'] = how much the items weighs.

['type'] = type of item it is, item, weapon etc...

['image'] = is the image you are using. Image should be located in the folder or it will not work! > This item image that is found in qb-inventory/html/images. Also make sure the name is the same as 'name'!
Don't write .png. The software will include the .png for you.

['unique'] = If the item can't be stacked and accepts item info to be assigned.

['useable'] =  if the item is useable. Consumeable for example.

['shouldClose'] = should the item close the inventory upon usage.

['combinable'] = nil - This part is not fully implemented. You should leave it as nil if you are not sure what to do.

['description'] = The item description.


Also asked for additional files if consumable is selected is:

['Minimum consumable value'] = Minimum value for the consumable.

['Maximum consumable value'] = Maximum value for the consumable.

['Define how it is consumed'] = Eat = Food, Drink = Drink, Custom is neither but something different. Would likely need to be modified with this option.



File outputs:
--Items goes to > [qb]/qb-core/shared

--Consumables goes to > [qb]/qb-smallresources/server

--Config goes to > [qb]/qb-smallresources

--Gsheets is an additional file that can be used for creating your own table in google sheets as a directory for personal usage.


Do not put these files directly into your folder! You should only copy and paste what is outputted and then insert it into their respective files.
Make sure you have a backup of these files before you do this.



This python script can be modified to what you need, please bare in mind I am very new to coding so it is pretty barebones. I just wanted something to use
to make item creating for qbcore easier.

To use it, please install python then open this file with Python. 
If your files are not outputting make sure you have the correct folder permissions before trying it. Try putting it in a folder rather than use it loose
on the desktop or on your harddrive.

This software is open source, under GNU General Public License. You can modify, redistribute as you see fit.
However under the original code it is not intended to be used as malicious software and I can't guarantee your pc safety if downloading from external sources.
