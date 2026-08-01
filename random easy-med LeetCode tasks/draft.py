nums = [3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]
player_1_score = 0
player_2_score = 0
i = 0
while nums:
    i += 1
    if len(nums) > 1:
        left_points = nums[0] - nums[1]
        right_points = nums[-1] - nums[-2]
        if left_points >= right_points:
            points = nums[0]
            nums = nums[1:]
        else:
            points = nums[-1]
            nums = nums[:-1]
    else:
        points = nums[0]
        nums = []
    if i % 2 == 1:
        player_1_score += points
    else:
        player_2_score += points
    print(player_1_score, player_2_score)
print(player_1_score >= player_2_score)

