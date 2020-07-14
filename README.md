# mac-commands

Scripts to change mac system settings. (Useful in case your keyboard is badly set).

In case you want to associate them with keyboard shortcuts:

1. Open automator (cmd+space, "automator")
2. Create a new "Quick Action" (or "Service" if it's an old version)
3. Drag "new shell script" from the list of actions
4. In "workflow receives", set "no input"
5. Then copy your python command (for example `/python/location /full/script/path`)
6. Save it.

Should be working now!

In case you want to associate a keyboard shortcut from the system, you can go
to "System preferences > Keyboard". Then it's the "Shortcuts" tab in "Services".
In the list, look for "General". In this category, your script's name should be
listed. Just add the shortcut and you should be good to go!
