img_path = arg[1]
 
mon = peripheral.find("monitor")
mon.setTextScale(0.5)
term.redirect(mon)
term.clear()
term.setCursorPos(1,1)
 
img = paintutils.loadImage("images/" .. img_path .. ".nfp")
paintutils.drawImage(img, 1, 1)