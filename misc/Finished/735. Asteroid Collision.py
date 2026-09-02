# https://leetcode.com/problems/asteroid-collision/submissions/

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                if abs(stack[-1]) == abs(i):
                    stack.pop()
                elif abs(stack[-1]) < abs(i):
                    stack.pop()
                    continue
                break
            else:
                stack.append(i)
        return stack


'''
class Solution:
    def asteroidCollision(self, asteroids):
        def sign(num):
            if num < 0:
                return 'Negative'
            else:
                return 'Positive'

        l, r = 0, 1
        while r < len(asteroids):
            ll = asteroids[l]
            rr = asteroids[r]
            if sign(ll) == sign(rr) or sign(ll) == 'Negative':
                l += 1
                r += 1
            else:
                if abs(ll) == abs(rr):
                    asteroids.pop(l)
                    asteroids.pop(l)
                    l, r = 0, 1
                elif abs(ll) > abs(rr):
                    asteroids.pop(r)
                    l, r = 0, 1
                elif abs(ll) < abs(rr):
                    asteroids.pop(l)
                    l, r = 0, 1
        return asteroids
'''