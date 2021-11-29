#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for

import os, random

app = Flask(__name__)
app.static_folder = "./static"
app.template_folder = "./templates"

@app.route("/")
def main():
    allFolders = os.listdir("./static/images/")
    return redirect(url_for("imageViewer", folderName=random.choice(allFolders)))

@app.route("/imageViewer/<string:folderName>")
def imageViewer(folderName):
    currentFolderPath = f"./static/images/{folderName}"
    if os.path.isdir(currentFolderPath):
        allFolders = os.listdir("./static/images/")
        temp, dirs, files = next(os.walk(currentFolderPath))

        if dirs != [] and files != []:
            return "Problem with folder structure for images", 500
        elif dirs != []:
            choosenFolder = random.choice(dirs)
            files = next(os.walk(f"{currentFolderPath}/{choosenFolder}"))[2]
        else:
            choosenFolder = "."

        random.shuffle(files)
        pathToFiles = [ f"./images/{folderName}/{choosenFolder}/{fileName}" for fileName in files ]
        return render_template("imageViewer.html", currentFolderName=folderName, folders=allFolders, imageList=pathToFiles)
    else:
        return "Folder doesn't seem to exist", 404






if __name__ == '__main__':
    app.run(debug=True)
