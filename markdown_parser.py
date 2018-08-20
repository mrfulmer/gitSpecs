# markdown_parser.py
# Author: Matthew Fulmer
# Date Created: 2018-08-15
# Description: Classes for parsing to and from markdown

import logging
import logging.config
import mistune
from time import strftime

class md2html():
    """Converts a markdown file (src) to and html and return a string. If a 
    destination file (dest) is provided, output will also be written to file"""

    def __inti__(self, src, dest=None):
        self.logger = logging.getLogger(__name__)
        self.src = src
        self.dest = dest

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def check(self):
        """Checks the markdown file for specification formatting"""
        self.logger.info("Beginning Markdown Check")
        

    def convert(self):
        """Converts the markdown to HTML string"""
        
        # Creating the markdown parser
        mistune.Markdown()


    def _writeHTML(self):
        """Writes the html string to a file"""


class html2md():
    def __inti__(self, src, fname):
        logging.getLogger(__name__)
        self.src = src
        self.file = fname


if __name__ == "__main__":
    # Setting up logger
    logname = "markdown_parser"
    dt = strftime(r"%Y%m%d")
    filepath = f"log/{dt}_{logname}.log"
    logging.config.fileConfig(
        fname="log/log.conf",
        defaults={'logfilename': filepath})



