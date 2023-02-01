# -*- coding: utf-8 -*-
import logging


def safe_close(fp):
    # 操作类函数，默认返回 None
    try:
        fp.close()
    except IOError:
        logger.warning("error closing file, ignore.")


# 日志模块再理解一下 https://zhuanlan.zhihu.com/p/360306588
logging.basicConfig(
    level=logging.DEBUG,
    filename="demo.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# logging.debug("This is  DEBUG !!")
# logging.info("This is  INFO !!")
# logging.warning("This is  WARNING !!")
# logging.error("This is  ERROR !!")
# logging.critical("This is  CRITICAL !!")

try:
    3 / 0
except Exception as e:
    # logging.error(e)
    logging.exception(e)
