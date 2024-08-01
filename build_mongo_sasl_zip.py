import os
import shutil
import glob

shutil.rmtree("dist")

os.makedirs("dist/bin")
os.makedirs("dist/include/sasl")
os.makedirs("dist/lib")

shutil.copyfile("win32/x64/Release/sasl2.dll", "dist/bin/sasl2.dll")
shutil.copyfile("win32/x64/Release/sasl2.pdb", "dist/bin/sasl2.pdb")
shutil.copyfile("win32/x64/Release/sasl2.lib", "dist/lib/sasl2.lib")

headers = glob.glob("include/*.h")
headers.append("win32/include/md5global.h")
for hdr in headers:
    filename = os.path.basename(hdr)
    shutil.copyfile(hdr, os.path.join("dist/include/sasl", filename))

shutil.make_archive("sasl", 'zip', "dist")