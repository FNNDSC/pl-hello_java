#
# hello_java ds ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
import os
import platform
import os.path,subprocess
from subprocess import STDOUT,PIPE
Gstr_title = r"""
 _          _ _            _                  
| |        | | |          (_)                 
| |__   ___| | | ___       _  __ ___   ____ _ 
| '_ \ / _ \ | |/ _ \     | |/ _` \ \ / / _` |
| | | |  __/ | | (_) |    | | (_| |\ V / (_| |
|_| |_|\___|_|_|\___/     | |\__,_| \_/ \__,_|
                  ______ _/ |                 
                 |______|__/                             
"""

Gstr_synopsis = """
(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS and TS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)
    NAME
       hello_java
    SYNOPSIS
        docker run --rm fnndsc/pl-hello_java hello_java                 \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 
    BRIEF EXAMPLE
        * Bare bones execution
            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-hello_java hello_java                     \
                /incoming /outgoing
    DESCRIPTION
        `hello_java` ...
    ARGS
        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.
        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
"""


class Hello_java(ChrisApp):
    """
    An app to display systen information
    """
    PACKAGE                 = __package__
    TITLE                   = 'An app to display systen information'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 1000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 200  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument(  '--name',
                            dest        = 'name',
                            type        = str,
                            optional    = True,
                            help        = "a simple string to print",
                            default     = "there")
        self.add_argument(  '--lines',
                            dest        = 'lines',
                            type        = str,
                            optional    = True,
                            help        = "number of lines to print",
                            default     = "0")

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        print('\n')
        

        self.compile_java('HelloWorld.java')
        
        self.execute_java('HelloWorld', options.name, options.lines)


    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


    def compile_java(self,java_file):
        subprocess.check_call(['javac', java_file])
        

    def execute_java(self,java_file, stdin,lines):
        java_class,ext = os.path.splitext(java_file)
        cmd = ['java', java_class, stdin,lines]
        proc = subprocess.run(cmd, stdout=PIPE, stderr=STDOUT)
        print (proc.stdout.decode("utf-8"))



