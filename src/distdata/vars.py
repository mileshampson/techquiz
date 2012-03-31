import distdata.connection

def getVar(name, default):
    scrapevars = __getScrapeVars()
    entry =  scrapevars.find_one(name)
    if entry is None:
        return default
    else:
        return entry["value"]
    
def setVar(name, value):
    scrapevars = __getScrapeVars()
    entry = scrapevars.find_one(name)
    if entry is None:
        entry = {"_id": name, "value": value }
    else:
        entry["value"] = value
    scrapevars.save(entry)
    

# internals

if __name__ == '__main__':
    setVar("test", "updated")
    print getVar("test", "default")
    