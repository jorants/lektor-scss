# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
import subprocess
import os
class ScssPlugin(Plugin):
    name = u'SCSS'
    description = u'Compiles files in /scss/ and places the result in /assets/static/.'

    def on_before_build_all(self, builder, **extra):
        sources = os.path.join(self.env.root_path, 'scss')
        dest = os.path.join(self.env.root_path, 'assets/static')
        for fn in os.listdir(sources):
            a,b,c = fn.rpartition(".")
            if c in ["scss","sass"]:
                full = os.path.join(sources,fn)
                out = os.path.join(dest,a+".css")
                subprocess.Popen(['sass',full,out]).wait()
