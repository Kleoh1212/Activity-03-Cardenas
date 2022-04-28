from logging import _Level


class pokestats():
    def statReturnHP(base,iv,ev,Level):
        return ((((2*base)+iv+(ev/4))*Level)/100)+Level+10

    def statReturnOtherStat(base,iv,ev,Level,nature):
        return((((2*base)+iv+(ev/4))*Level/100)+5)*nature