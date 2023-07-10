#!/usr/bin/python3

import dbus
import dbus.mainloop.glib
import dbus.service
from gi.repository import GLib

AGENT_PATH = "/org/bluez/AuthorizeServiceAgent"
AGENT_INTERFACE = 'org.bluez.Agent1'
CAPABILITY = "DisplayYesNo"
# CAPABILITY = "NoInputNoOutput"

class Agent(dbus.service.Object):
    @dbus.service.method(AGENT_INTERFACE, in_signature="os", out_signature="")
    def AuthorizeService(self, device, uuid):
        print("AuthorizeService %s %s" % (device, uuid))
        return
        if uuid == "0000111f-0000-1000-8000-00805f9b34fb":
            print("Whitelisted")
            return
        print("Rejected")
        raise dbus.DBusException("AuthorizeService rejected")

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    agent = Agent(bus, AGENT_PATH)
    obj = bus.get_object("org.bluez", "/org/bluez")

    manager = dbus.Interface(obj, "org.bluez.AgentManager1")
    manager.RegisterAgent(AGENT_PATH, CAPABILITY)
    manager.RequestDefaultAgent(AGENT_PATH)

    GLib.MainLoop().run()
