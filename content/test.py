ans = float("inf")
mln = float("inf")
mnw = float("inf")

for i in range(len(landStartTime)):
    mln = min(mln, landStartTime[i] + landDuration[i])

for i in range(len(waterStartTime)):
    ans = min(ans, max(mln, waterStartTime[i]) + waterDuration[i])

for i in range(len(waterStartTime)):
    mnw = min(mnw, waterStartTime[i] + waterDuration[i])

for i in range(len(landStartTime)):
    ans = min(ans, max(mnw, landStartTime[i]) + landDuration[i])
