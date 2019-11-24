from math import cos, sin, atan2, pi, log


def get_frequency_response(b, a: list = None, k: float = 1, steps: int = 1001):
    if not a:
        a = [0]
    A = len(a)
    B = len(b)
    W = [i / steps for i in range(steps)]
    magnitude = []
    phase = []
    for w in W:
        w *= pi
        ar = sum([ha * cos((1 - A + na) * w) for ha, na in zip(a, range(A))])
        br = sum([hb * cos((1 - B + nb) * w) for hb, nb in zip(b, range(B))])
        aj = sum([ha * sin((1 - A + na) * w) for ha, na in zip(a, range(A))])
        bj = sum([hb * sin((1 - B + nb) * w) for hb, nb in zip(b, range(B))])
        H = complex(br, bj) / complex(ar, aj)
        magnitude.append(k * abs(H))
        phase.append(-atan2(H.imag, H.real))
    return magnitude, phase, W


def generate_signal(f, fs, A, DC, t_final, t_steps=1000):
    """
    Generate a signal with specified specifications
    :param f: the signal's frequency
    :param fs: the sampling frequency
    :param A: the sine wave amplitude
    :param DC: an added dc component of the signal
    :param t_final: final time for signal.
    :param t_steps: number of steps for time vector
    :return: x(n), t(n), x(t), t
    """
    w = 2 * pi * f / fs
    T = [t_final * i / t_steps for i in range(t_steps)]
    N = int(t_final * fs)
    tn = [i / fs for i in range(N)]
    xn = [A * sin(w * n) + DC for n in range(N)]
    xt = [A * sin(2 * pi * f * t) + DC for t in T]
    return xn, tn, xt, T


def add_signals(sig1: list, sig2: list):
    if len(sig1) != len(sig2):
        return None
    return [s1 + s2 for s1, s2 in zip(sig1, sig2)]


def amplitude2db(amp: list):
    db = [20 * log(a, 10) for a in amp]
    return db


def db2amplitude(db: list):
    amp = [pow(10, (d / 20)) for d in db]
    return amp
