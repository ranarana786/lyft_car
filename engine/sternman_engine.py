from abc import ABC

import base_engine


class SternmanEngine(base_engine.Engine):
    def __init__(self,warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
