# gitSpec.py
# env
# Author: Matthew Fulmer
# Date: 2018-14-2018
# 

import logging
import markdown_parser
import html_parser
import docx_parser
from time import strftime




if __name__ == "__main__":
    # Setting up logger
    logname = "gitSpec"
    dt = strftime("%Y%m%d")
    LOG_FILE = f"log/{dt}_{logname}.log"
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = LOG_FILE,
                        filemode = 'w',
                        format = LOG_FORMAT,
                        datefmt = '%Y-%m-%d %H:%M:%S',
                        level = logging.DEBUG)
