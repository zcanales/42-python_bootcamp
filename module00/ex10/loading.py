import time

"""def ft_progress(lst):
    index = 1
    start = time.time()
    total = len(lst)
    for i in lst:
        pourcent = int(index / total * 100)
        elapsed_time = time.time() - start
        eta = (elapsed_time * total / index) - elapsed_time
        progress_length = int(20 * index // total)
        progress = "=" * progress_length + '>' + ' ' * (20 - progress_length)
        print(f"\rETA: {eta:4.2f}s [{pourcent:3}%][{progress}] \
{index:{len(str(total))}}/{total} | elapsed time {elapsed_time:.2f}s", end='')
        index += 1
        yield i"""

def ft_progress(lst):
    index = 1
    start = time.time()
    total = len(lst)
    for i in lst:
        progress = int(i / total * 100)
        time_now = time.time() - start
        progress_length = int(progress / 2)
        progress_print = '=' * progress_length + '>'
        print(f"\rETA: {time_now:4.2f}s {progress:3d}% [{progress_print}] {i}/{total}", end='')
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
