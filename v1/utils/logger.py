#  Unisoft Group Copyright (c) 2022/11/9
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import datetime
import json
import time

from django.conf import settings

from v1.services import telegram

total_time = 0


class Logger:
    """If a log file for today already exist, open it in append mode.
    Else, create a new log file for today, and open it in append mode.
    """
    DEBUG = False
    PADDING = 9
    FORMAT = f"----------------------------------------------------------------" \
             f"\nTIME: {{datetime:%I:%M:%S}} {{msg}}\n"

    def __init__(self, name, debug, padding, format_: str = None):
        my_dir = settings.LOGS_DIR
        for part in name.split('.'):
            my_dir = my_dir / part
            if not my_dir.exists():
                my_dir.mkdir()
        self.dir = my_dir
        self.DEBUG = debug
        self.PADDING = padding
        if not (format_ is None):
            self.FORMAT = format_.format(self.PADDING)

    @property
    def file_name(self):
        return self.dir / f'{datetime.datetime.now():%Y-%m-%d}.log'

    # @extra_log
    def log(self, msg, level):
        if not self.DEBUG and level == "DEBUG":
            return
        # file = self.file
        # file.open()
        # self.FILE.write(self.FORMAT.format(
        #     type=level,
        #     msg=msg,
        #     datetime=datetime.datetime.now(),
        # ))
        with open(self.file_name, "a+", encoding='utf8') as file:
            file.write(self.FORMAT.format(
                type=level,
                msg=msg,
                datetime=datetime.datetime.now(),
            ))
        # file.close()

    # @count
    def info(self, msg):
        """Log info"""
        self.log(msg, "INFO")

    def update(self, msg):
        "Used to log whenever a state is updated"
        self.log(msg, "UPDATE")

    def exception(self, msg):
        self.log(msg, "EXCEPTION")

    def debug(self, msg):
        "Only logs if the static variable {DEBUG} is set to True."
        self.log(msg, "DEBUG")

    def clear(self):
        """Clears the log file"""
        self.FILE.truncate(0)

    # @extra_log
    def object(self, object):
        """Intended for use on objects. They usually have a lot of information;
        therefor, we enclose the information with lines to make the log more readable."""
        with open(self.file_name, "a+") as file:
            file.write(
                f"-----------------------       object log\n"
                + str(object)
                + f"\n-----------------------\n"
            )

    def api_request(self, request, response=None, start_time=0):

        data = json.loads(request.body.decode("utf-8"))
        duration = time.time() - start_time
        duration = round(duration, 2)
        message = f"\nHost: {request.get_host()}  " \
                  f"\nClient: {request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()} " \
                  f"\nMethod: {request.method} " \
                  f"\nPath: {request.get_full_path()}" \
                  f"\nDuration: {duration} s" \
                  f"\nRequest:  {json.dumps(data, ensure_ascii=False)}" \
                  f"\nResponse: {json.dumps(response, ensure_ascii=False)}"

        if duration > 15:
            try:
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                print(ip)

                telegram.notify(message, '-860055013')
            except Exception:
                pass
        self.info(message)

    def api_service_request(self, request, response=None, start_time=0):
        duration = time.time() - start_time
        duration = round(duration, 2)
        message = f"\nDuration: {duration} s" \
                  f"\nRequest:  {json.dumps(request, ensure_ascii=False)}" \
                  f"\nResponse: {json.dumps(response, ensure_ascii=False)}"

        if duration > 15:
            try:
                telegram.notify(message, '-824826991')
            except Exception:
                pass

        self.info(message)


if __name__ == "__main__":
    logger = Logger(__name__, True, 10)
    logger.info("This is a test")
    logger.info("running something")
    logger.debug("Some debugging details")
    logger.exception("Critical error!")
    logger.debug("Some more debugging details")
    time.sleep(60)
    logger.info("This is a test")
    logger.info("running something")
    logger.debug("Some debugging details")
    logger.exception("Critical error!")
    logger.debug("Some more debugging details")
