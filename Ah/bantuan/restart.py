import asyncio
import contextlib
import math
import os
import shlex
import shutil
import time

async def restart(
    update: bool = False,
    clean_up: bool = False,
    shutdown: bool = False,
):
    try:
        shutil.rmtree(Config.DWL_DIR)
        shutil.rmtree(Config.TEMP_DIR)
    except BaseException:
        pass

    if clean_up:
        os.system(f"mkdir {Config.DWL_DIR}")
        os.system(f"mkdir {Config.TEMP_DIR}")
        return

    if shutdown:
        return os.system(f"kill -9 {os.getpid()}")

    cmd = (
        "git pull && && bash tai.sh"
        if update
        else "bash tai.sh"
    )

    os.system(f"kill -9 {os.getpid()} && {cmd}")
