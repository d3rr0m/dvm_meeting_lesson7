def render_progressbar(
        total,
        iteration, prefix='',
        suffix='',
        length=30,
        fill='█',
        zfill='░',
        ):

    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    print(render_progressbar(
        20,
        3,
        prefix='prefix',
        suffix='suffix',
        length=100,
        ))
