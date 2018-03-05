
def mzMenu():
    ret = {"type"     : "command",
           "menu"     : "Marza",
           "name"     : "Pipeline/Open Shot",
           "icon"     : "ColorTransfer.png",
           "command"  : "import openShot; openShot.main()"}
    
    return [ret]
