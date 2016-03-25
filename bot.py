import sys
import time
import telepot
from NexTrip import NexTrip

run = True


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print content_type, chat_type, chat_id
    if 'text' in msg and msg['text'][0] == "/":
        text = msg['text']
        user = msg['from']
        elements = text.strip().split(" ")
        cmd = elements[0][1:]
        args = elements[1:]
        print cmd
        print args
        if cmd == "departures":
            if len(args) == 1:
                departs = nt.departures(int(args[0]))
                ret = ""
                for depart in departs:
                    ret += depart.route + " | " + depart.description + " | " + depart.departureText + "\n"
                bot.sendMessage(user['id'], ret)
        elif cmd == "stop":
            bot.run = False

if __name__ == "__main__":
    token = sys.argv[1]
    nt = NexTrip()
    bot = telepot.Bot(token)
    bot.notifyOnMessage(handle)
    # run = True
    print 'Listening...'
    while run:
        time.sleep(1)
    print "Stopping"
    exit()
