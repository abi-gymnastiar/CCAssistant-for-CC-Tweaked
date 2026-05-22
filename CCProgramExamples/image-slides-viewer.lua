local dir, interval = arg[1], arg[2]
if dir == nil then
    dir = "images"
end
 
if interval == nil then
    interval = "5"
end
interval = tonumber(interval)
 
local mon = peripheral.find("monitor")
 
local files = fs.list(dir)
 
local i = 1
mon.setTextScale(0.5)
term.redirect(mon)
 
local images = {}
for _, file in ipairs(files) do
    local img = paintutils.loadImage(dir .. "/" .. file)
    table.insert(images, img)
end
 
while i ~= 0 do
    term.clear()
    term.setCursorPos(1,1)
    paintutils.drawImage(images[i], 1, 1)
    i = i + 1
    if i > #images then
        i = 1
    end
    os.sleep(interval)
end