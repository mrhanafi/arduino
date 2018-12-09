import git, os, shutil

DIR_NAME = "/home/pi/git/arduino"
REMOTE_URL = "https://github.com/mrhanafi/arduino.git"

#if os.path.isdir(DIR_NAME):
#	shutil.rmtree(DIR_NAME)

#os.mkdir(DIR_NAME)

repo = git.Repo.init(DIR_NAME)
#origin = repo.create_remote('origin',REMOTE_URL)
origin = repo.remotes.origin
origin.fetch()
origin.pull(origin.refs[0].remote_head)

print "-- Done --"
