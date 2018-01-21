#Written by Chris Penn 21/01/18 MB Transport.


from mcpi.minecraft import Minecraft
import time
import random
import microbit

mc = Minecraft.create()

LineColour = 46#block type of powered blocks

    
while True:
    while microbit.button_a.is_pressed() == True:#while a button being pressed keep going fwd
        x,y,z = mc.player.getPos()
        #get block -1
        CurrentBlock = mc.getBlock(x,y-1,z)
        #Go straight ahead
        #if block -1 == 46 then
        if CurrentBlock == 46 & mc.getBlock(x,y-1,z-1)== 46:#1ststraight
            mc.player.setPos(x,y,z-1)
        if CurrentBlock == 46 & mc.getBlock(x,y+1,z+1)== 46:#1ststraight
            mc.player.setPos(x,y+1,z+1)

    if  microbit.button_b.was_pressed():
        mc.player.setPos(-80,81,-244)
        
