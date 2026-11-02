


screen MapUI():
    modal True

    add "map/map new.png" xysize (config.screen_width, config.screen_height)

    imagebutton:
        xpos 1374
        ypos 214
        idle "map/test.png"
        hover "map/test.png"
        action [
            SetVariable("map_open", False),
            Stop("music"),
            Jump("acookingland")
        ]
    key "K_m" action SetVariable("map_open", False)


    # Continue your story here.


