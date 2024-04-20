def convert_minMax_actual_to_desired(
    minOutputActual,
    maxOutputActual,
    minOutputDesired,
    maxOutputDesired,
    outputValue,
):
    # slope of line (m): (y2 - y1) / (x2 - x1)
    y2 = maxOutputDesired
    y1 = minOutputDesired
    x2 = maxOutputActual
    x1 = minOutputActual

    # slope of line (m) = (y2 - y1) / (x2 - x1)
    m = (y2 - y1) / (x2 - x1)
    # y - y1 = m(x - x1)
    y = m * (outputValue) - m * x1 + y1

    print("m", m, "y", y, "outputValue", outputValue)

    # handle inaccurate "lowest possible" output value
    if y < minOutputDesired:
        y = minOutputDesired

    # handle inaccurate "highest possible" output value
    if y > maxOutputDesired:
        y = maxOutputDesired

    return y
