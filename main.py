import filter as f
from matplotlib import pyplot as plt

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

filt = f.Filter(b, a=a)
step = [1] * 160
impulse = [1] + [0] * 159
step_response = filt.filter_list(step)
filt.clear()
impulse_response = filt.filter_list(impulse)

mag, phase, W = f.get_frequency_response(b, a=a)
db = f.amplitude2db(mag)

plt.figure()
plt.plot(W, db)
plt.show()

plt.figure()
plt.plot(step_response)
plt.show()

plt.figure()
plt.plot(impulse_response)
plt.show()