import filter as fi
from matplotlib import pyplot as plt


def main():
    num = [0.00025421634845499124,
           -0.00079187872147285572,
           0.00141377112114653320,
           -0.00167945032088055311,
           0.00176640706253605641,
           -0.00167945032088055311,
           0.00141377112114653320,
           -0.00079187872147285572,
           0.00025421634845499124]

    den = [1,
           -6.142345166576267168068,
           16.682363664620424970053,
           -26.134169993147157384782,
           25.804074652366246311885,
           -16.430866660921950028750,
           6.584876413720856191957,
           -1.517738749625560545908,
           0.153965563480438771826]

    b = num
    a = den
    filt = fi.Filter(b, a=a)

    step = [1] * 160
    impulse = [1] + [0] * 159
    Om = 0.3  # * pi (rad / sample)
    fs = 100
    f = Om / 2 * fs
    print(f, f/10)
    xn1, tn, xt1, t = fi.generate_signal(f, fs, 0.2, 0, 5)
    xn2, tn2, xt2, t2 = fi.generate_signal(f / 10, fs, 1, 0, 5)
    xn = fi.add_signals(xn1, xn2)
    xt = fi.add_signals(xt1, xt2)

    step_response = filt.filter_list(step)
    filt.clear()
    impulse_response = filt.filter_list(impulse)
    filt.clear()
    yn = filt.filter_list(xn)

    mag, phase, W = fi.get_frequency_response(b, a=a)
    db = fi.amplitude2db(mag)

    plt.figure()
    plt.plot(W, db)

    plt.figure()
    plt.plot(W, phase)

    plt.figure()
    plt.plot(step_response)

    plt.figure()
    plt.plot(impulse_response)

    plt.figure()
    plt.plot(t, xt)
    plt.plot(tn, yn)

    plt.show()


if __name__ == '__main__':
    main()
