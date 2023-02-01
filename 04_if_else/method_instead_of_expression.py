# 活动：如果活动还在开放，并且活动剩余名额大于 10，为所有性别为女性，或者级别大于 3 的活跃用户发放 10000 个金币
if activity.is_active and activity.remaining > 10 and user.is_active and (user.sex == "female" or user.level > 3):
    user.add_coins(10000)
    return


if activity.allow_new_user() and user.match_activity_condition():
    user.add_coins(10000)
    return

# python 3.10 Structural Pattern Matching 结构化模式匹配
# https://blog.csdn.net/gongjianbo1992/article/details/122754872
# 模式匹配的通用语法如下:
"""
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
"""
