# gitSpec.py
# env
# Author: Matthew Fulmer
# Date: 2018-14-2018
# 

import logging
import logging.config
import markdown_parser
import docx_parser
from time import strftime




if __name__ == "__main__":
    # Setting up logger
    logname = "gitSpec"
    dt = strftime(r"%Y%m%d")
    filepath = f"log/{dt}_{logname}.log"
    logging.config.fileConfig(
        fname="log/log.conf",
        defaults={'logfilename': filepath})
