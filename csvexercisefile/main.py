file = None

with open('data.csv') as d:
    file = d.read()


data = file.split("\n")


missing_NA = 0
steps_dict = {}
interval_dict = {}
steps_perday = []
steps_perday2 = []
steps_dict2 = {}
interval = 0
interval_perday = []
mean_dict = {}

# Steps
for line in range(len(data)):
    value = data[line].split(",")
    if line == 0:
        pass
    else:
        if len(value) < 3:
            continue
        if value[0] == 'NA':
            missing_NA += 1
            steps_dict.setdefault(value[1], 0)
            steps_dict2.setdefault(value[1], 0)
            interval_dict.setdefault(value[1], 0)
            steps_dict[value[1]] = 0
            interval_dict[value[1]] += 1

        else:
            steps_dict.setdefault(value[1], 0)
            steps_dict2.setdefault(value[1], 0)
            interval_dict.setdefault(value[1], 0)
            mean_dict.setdefault(value[1], 0)
            steps_dict[value[1]] += int(value[0])
            interval_dict[value[1]] += 1

for steps in steps_dict.values():
    steps_perday.append(steps)

for interval_value in interval_dict.values():
    interval_perday.append(interval_value)

# Mean
def mean(steps_perday, interval_perday):
    return steps_perday // interval_perday


print('Total steps taken per day:', steps_dict)
print('Total missing NA:', missing_NA)


mean = map(mean, steps_perday, interval_perday)
print('Mean:', list(mean))

total_mean = round(sum(steps_perday)/sum(interval_perday), 3)
print('Total mean:', total_mean)


# Median
median = None
n = len(steps_perday)
steps_perday.sort()


if n % 2 == 0:
    median1 = steps_perday[n//2]
    median2 = steps_perday[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = steps_perday[n//2]

print('Median:', median)

# New dataset
res = {}
for line in range(len(data)):
    value = data[line].split(",")
    if line == 0:
        pass
    else:
        if len(value) < 3:
            continue
        for x in range(len(value)):
            if value[1] in res:
                if value[0] != 'NA':
                    res.setdefault(value[1], 0)
                    res[value[1]][0] += int(value[0])
                    res[value[1]][2][value[2]] = int(value[0])
                else:
                    res[value[1]][1] += 1
                    res[value[1]][2][value[2]] = 0
            else:
                if value[0] != 'NA':
                    res[value[1]] = [int(value[0]), 0, {value[2]: value[0]}]
                else:
                    res[value[1]] = [0, 1, {value[2]: 0}]

print('New dataset:', res)

# Weekday/Weekend
for_day = []
for_day2 = []
for line in range(1, len(data)):
    value = data[line].split(",")
    if line == 0:
        pass
    else:
        if len(value) < 3:
            continue
        for_day.append(value[1])
        for_day2.append(value[1])


for_day = list(dict.fromkeys(for_day))
for_day2 = list(dict.fromkeys(for_day2))
day = ','.join(for_day2)
one_day = day.split(',')

count_day = 1
for i in range(len(for_day)):
    if count_day > 7:
        count_day = 1

    if count_day <= 5:
        for_day[i] = "Weekday"
        count_day += 1
    else:
        for_day[i] = "Weekend"
        count_day += 1

zipfor_day = zip(one_day, for_day)
dict_day = dict(zipfor_day)
print('Weekday/Weekend:', dict_day)