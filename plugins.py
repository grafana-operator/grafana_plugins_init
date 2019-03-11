#!/bin/env python

import os
import zipfile
import urllib.request
import shutil

pluginsKey = "GRAFANA_PLUGINS"
pluginsVolume = "/opt/plugins"

def getPlugins():
    result = list()
    if pluginsKey in os.environ and not (not os.environ[pluginsKey]):
        plugins = os.environ[pluginsKey].split(",")
        for plugin in plugins:        
            parts = plugin.split(":")
            if len(parts) == 2:
                result.append((parts[0], parts[1]))
            else:
                print("Invalid syntax (version missing?): " + plugin)
    return result

def downloadPlugin(plugin):
    url = "https://grafana.com/api/plugins/%s/versions/%s/download" % plugin
    file_name = "/tmp/%s_%s.zip" % plugin
    with urllib.request.urlopen(url) as response, open(file_name, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
    return file_name

def extractPlugin(file_name):
    zip = zipfile.ZipFile(file_name)
    zip.extractall(pluginsVolume)
    zip.close()

def installPlugin(plugin):
    try:
        file_name = downloadPlugin(plugin)
    except:
        print("Error downloading %s:%s" % plugin)
    else:
        extractPlugin(file_name)

def main():
    for plugin in getPlugins():
        installPlugin(plugin)

main()
