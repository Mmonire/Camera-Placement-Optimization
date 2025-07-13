import random

# تعریف نقاط
points = [f'p{i}' for i in range(1, 201)]
print("points:", ", ".join(points))

# تعداد گروه‌های اولیه به صورت تصادفی بین 80 تا 250
num_groups = random.randint(20, 50)

# ایجاد گروه‌های اولیه
groups = [[] for _ in range(num_groups)]

# تخصیص اولیه: هر نقطه حداقل یک بار در گروه‌های اولیه استفاده شود
random.shuffle(points)
for i, point in enumerate(points):
    groups[i % num_groups].append(point)

# اطمینان از استفاده تمام نقاط
remaining_points = [p for p in points if all(p not in group for group in groups)]

# تکمیل گروه‌های موجود: هر گروه باید بین 2 تا 5 نقطه داشته باشد
for group in groups:
    while len(group) < random.randint(3, 4):
        if remaining_points:
            group.append(remaining_points.pop())

# اطمینان از داشتن تعداد گروه‌های هدف (مثلاً 500 گروه)
target_groups = 100

# ایجاد گروه‌های اضافی
while len(groups) < target_groups:
    group_size = random.randint(3, 4)  # تعداد نقاط هر گروه بین 2 تا 5
    new_group = random.sample(points, group_size)
    groups.append(new_group)

random.shuffle(groups)
# تولید هزینه برای هر گروه و نمایش خروجی
output = []
for i, group in enumerate(groups):
    group_str = f'c{i+1}: {", ".join(group)}'
    output.append(group_str)
# چاپ گروه‌ها
for group in output:
    print(group)
