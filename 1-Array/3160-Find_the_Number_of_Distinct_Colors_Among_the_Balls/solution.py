class Solution:
    def queryResults(self, limit, queries):
        ball_color = {}
        colors_count = {}
        result = []

        for ball, color in queries:
            if ball in ball_color:
                old_color = ball_color[ball]
                colors_count[old_color] -= 1
                if colors_count[old_color] == 0:
                    del colors_count[old_color]

            ball_color[ball] = color

            if color in colors_count:
                colors_count[color] += 1
            else:
                colors_count[color] = 1

            result.append(len(colors_count))

        return result     
