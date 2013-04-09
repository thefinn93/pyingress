#!/usr/bin/env python
from ingress import Ingress
from termcolor import colored
import code

def prettychat(chatobj):
    data = chatobj['plext']['markup']
    prettyline = ""
    for i in data:
        if i[0] is "SECURE":
            prettyline += colord(i[1]['plain'], 'red')
        elif i[0] is "SENDER":
            prettyline += colord(i[1]['plain'], 'green')
        else:
            prettyline += i[1]['plain']
    return prettyline

ingress = Ingress()
chat = ingress.rpc({"desiredNumItems":50,"minLatE6":47747238,"minLngE6":-122323110,"maxLatE6":47804919,"maxLngE6":-122095830,"minTimestampMs":1364517824731,"maxTimestampMs":-1,"factionOnly":False,"ascendingTimestampOrder":True,"method":"dashboard.getPaginatedPlextsV2"})
for line in chat['result']:
    print prettychat(line[-1])

code.interact(local=locals())
