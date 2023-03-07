QBcore-Item-Printer does exactly what is says.
A simple Python script to empower users in making items more efficiently. Decided on because creating 3 unique .txt files everytime would be incredibly time consuming.
Hopefully this helps some of you create projects a little easier.
See some of the example outputs in the .txt files provided.

See below example from qbcore website:
QBShared.Items = {
    ['id_card'] = {
        ['name'] = 'id_card', -- Actual item name for spawning/giving/removing
        ['label'] = 'ID Card', -- Label of item that is shown in inventory slot
        ['weight'] = 0, -- How much the items weighs
        ['type'] = 'item', -- What type the item is (ex: item, weapon)
        ['image'] = 'id_card.png', -- This item image that is found in qb-inventory/html/images (must be same name as ['name'] from above)
        ['unique'] = true, -- Is the item unique (true|false) - Cannot be stacked & accepts item info to be assigned
        ['useable'] = true, -- Is the item useable (true|false) - Must still be registered as useable
        ['shouldClose'] = false, -- Should the item close the inventory on use (true|false)
        ['combinable'] = nil, -- Is the item able to be combined with another? (nil|table)
        ['description'] = 'A card containing all your information to identify yourself' -- Description of time in inventory
    }
}

-- Example of an item that is combinable and not nil

['combinable'] = {
    accept = {'snspistol_part_1'}, -- The other item that can be it can be combined with
    reward = 'snspistol_stage_1', -- The item that is rewarded upon successful combine
    anim = { -- Set the animation, progressbar text and length of time it takes to combine
        ['dict'] = 'anim@amb@business@weed@weed_inspecting_high_dry@', -- The animation dictionary
        ['lib'] = 'weed_inspecting_high_base_inspector', -- The animation library
        ['text'] = 'Atttaching attachments', -- Text that will be displayed in the progress bar
        ['timeOut'] = 15000,} -- How long the animation should take to complete
    }
}


This python script will show you a console to take you through each entry.
['name'] = what is used for spawning. It should not have a space in the name use '_' or '-' instead.
['label'] = what is used ingame, so what the player will see.
['weight'] = how much the items weighs.
['type'] = type of item it is, item, weapon etc...
['image'] = is the image you are using. Image should be located in the folder or it will not work! > This item image that is found in qb-inventory/html/images.
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
