#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # `ans` will store the final asteroids that survive without any collisions
        ans = []
        
        # `stack` will hold the asteroids moving to the right
        stack = []

        # Iterate through each asteroid
        for x in asteroids:
            # Asteroid moving to the right
            if x > 0:
                stack.append(x)
            # Asteroid moving to the left
            else:
                # Continue popping from the stack until we find an asteroid moving to the right
                # that is bigger than the current asteroid (or the stack is empty).
                # This simulates all collisions for the current asteroid moving left.
                while stack and stack[-1] < abs(x):
                    stack.pop()

                # If the stack is empty after all possible collisions, it means the current
                # asteroid moving left survived and will be added to the `ans`.
                if not stack:
                    ans.append(x)
                # If the top of the stack is the same size as the current asteroid (but moving right),
                # both asteroids explode. So, we pop the top asteroid from the stack.
                elif stack[-1] == abs(x):
                    stack.pop()

        # After processing all asteroids, append any remaining right-moving asteroids from the stack to `ans`
        ans += stack
        
        return ans

# @lc code=end

