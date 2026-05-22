local audioname, intervalRangeMin, intervalRangeMax = arg[1], tonumber(arg[2]) or 0.1, tonumber(arg[3]) or 0.1
local dfpwm = require("cc.audio.dfpwm")
local speaker = peripheral.find("speaker")

local decoder = dfpwm.make_decoder()
while true do
    for chunk in io.lines("audios/" .. audioname .. ".dfpwm", 16 * 1024) do
       local buffer = decoder(chunk)
       while not speaker.playAudio(buffer) do
           os.pullEvent("speaker_audio_empty")
       end
    end
    os.sleep(math.random(intervalRangeMin, intervalRangeMax))
end