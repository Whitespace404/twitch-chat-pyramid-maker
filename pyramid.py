from twitchobserver import Observer
from time import sleep as wait

observer = Observer('<enter your twitch username here>', 'oauth:*****')
channel = "<enter channel name here>"
pyramid_width = 3
pyramid_text = "Kappa "

observer.start()
observer.join_channel(channel)

for i in range(1, pyramid_width + 1):
   observer.send_message(pyramid_text * i, channel)
   for event in observer.get_events():
       if event == "TWITCHCHATMESSAGE" and event.nickname != "<enter your twitch username here>":
           quit()
   wait(1)

for k in range(pyramid_width, 0, -1):
    for event in observer.get_events():
       if event == "TWITCHCHATMESSAGE" and event.nickname != "<enter your twitch username here>":
           quit()

    observer.send_message(pyramid_text * k, channel)
    wait(1)

observer.leave_channel(channel)
quit()
