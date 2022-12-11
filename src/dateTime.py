#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa



def hourToInt(time):
    """

    """
    t = time.split(":")
    return int(t[0])



def minutesToInt(time):
    """

    """
    t = time.split(":")
    return int(t[1])    


def intToTime(hour, minutes):
    """

    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m










