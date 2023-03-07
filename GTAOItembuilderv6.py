import os
import math

print(os.getcwd())
print("==============================|QbCore-Item-Printer|============================== \n A powerful tool designed to assist in the creation of items. Prints 3 different \n files to be placed in their respective .lua files. \n see below: \n \n --Items goes to > [qb]/qb-core/shared \n --Consumables goes to > [qb]/qb-smallresources/server \n --Config goes to > [qb]/qb-smallresources \n \nDo not replace the files!! You must edit the notepad and find their appropriate places. Then copy and paste.\n \n \nTool created by Aercascade#4928")

while True:
    name = input("enter anything or specify exit to close application ")
    if name == 'exit':
        break


    file1 = 'items'
    file1_path = os.path.join(os.getcwd(), file1)

    file2 = 'config'
    file2_path = os.path.join(os.getcwd(), file2)

    file3 = 'consumables'
    file3_path = os.path.join(os.getcwd(), file3)
    
    file4 = 'gsheets'
    file4_path = os.path.join(os.getcwd(), file4)

    name = input("Enter the name of the item (must be lower case and without spaces): ")
    label = input("Enter the label of the item (used for the ingame name): ")
    weight = int(input("Enter the weight of the item (Base: 100): "))
    type = input("Enter the type of the item (Base: type): ")
    image = input("Enter the name of the image file (without .png, file type must be png): ")
    unique = input("Is the item unique? Enter true or false - MUST BE LOWERCASE: ")
    useable = input("Is the item useable? Enter true or false - MUST BE LOWERCASE: ")
    shouldClose = input("Should the item close? Enter true or false - MUST BE LOWERCASE: ")
    combinable = input("Enter the name of the combinable item: if none input as nil ")
    description = input("Enter a description of the item:  ")

    item = {
        'name': name,
        'label': label,
        'weight': weight,
        'type': type,
        'image': image,
        'unique': unique,
        'useable': useable,
        'shouldClose': shouldClose,
        'combinable': combinable,
        'description': description
}


    output = "    ['" + name + "']                           = {"
    output += "['name'] = '" + name + "',    "
    output += "['label'] = '" + label + "', 			  	  	"
    output += "    ['weight'] = " + str(weight) + ", 			"
    output += "    ['type'] = '" + type + "', 		"
    output += "    ['image'] = '" + image + ".png', 		"
    output += "    ['unique'] = " + str(unique) + ", 		"
    output += "    ['useable'] = " + str(useable) + ",    "
    output += "    ['shouldClose'] = " + str(shouldClose) + ", 		"
    output += "    ['combinable'] = " + str(combinable) + ", 		" 		
    output += "    ['description'] = '" + description + "' 		"
    output += "},\n"

    save = input("Would you like to save? specify y/n ")
    if save == "y" or save == "yes" or save == "YES" or save == "Y":
        with open('items.txt', 'a') as f:
            f.write(output)
            print("\n Data written to Items.txt \n \n")
    elif save != "y" or save != "yes" or save != "YES" or save != "Y":
        break
    else:
        break

    if useable == "true":
        mathvaluemin = input("Enter a minimum consumable value (water/sandwich is 35):  ")
        mathvaluemax = input("Enter a maximum consumable value (water/sandwich is 54):  ")
        consume = input("Define how it is consumed, Eat, Drink or Custom  ")
        item = {
            'mathvaluemin': mathvaluemin,
            'mathvaluemax': mathvaluemax,   
        }
        output = '    ["' + name + '"] = math.random(' + str(mathvaluemin) + ', ' + str(mathvaluemax) + '),\n'
        with open('config.txt', 'a') as f:
            f.write(output)                

        output = 'QBCore.Functions.CreateUseableItem("' + name + '", function(source, item)\n'
        output += '\tlocal Player = QBCore.Functions.GetPlayer(source)\n'
        output += '\tif Player.Functions.RemoveItem(item.name, 1, item.slot) then\n'
        output += '\t\tTriggerClientEvent("consumables:client:'+ consume +'", source, item.name)\n'
        output += '\tend\n'
        output += 'end)\n'

        with open('consumables.txt', 'a') as f:
            f.write(output)
            
        output = '' + name + '	'
        output += '' + label + '	'
        output += '' + str(weight) + '	'
        output += '' + type + '	'
        output += '' + image + ".png	"
        if useable == "true":
            output += '' + str(mathvaluemin) + ',' + str(mathvaluemax) + ' '
            if consume == "Eat":
                output += 'Food '
            elif consume == 'Drink':
                output += 'Drink '
            elif consume == 'Custom':
                output += 'Custom '
        else:
            output += ''  ''
            output += ''  ''
        output += '' + description + '\n'
        
        with open('gsheets.txt', 'a') as f:
            f.write(output)        
        
            print("Process complete, Begin next item?\n \n")
