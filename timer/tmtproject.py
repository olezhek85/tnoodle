import tmt
import subprocess
from os.path import join, exists
import shutil

class Project(tmt.EclipseProject):
	def configure(self):
		tmt.EclipseProject.configure(self)
		tmt.WinstoneServer.addPlugin(self)

		# I'd rather maintain a single TNoodle.jar binary that multiple different
		# jars with different subsets of what I consider TNoodle.
		self.fullName = "TNoodle"

Project(tmt.projectName(), description="A Rubik's Cube timer.")
