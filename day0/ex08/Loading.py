import sys
import time
from shutil import get_terminal_size


def format_time(t: float) -> str:
    """ a simple function to return time in min02:sec02 format"""
    mins, secs = divmod(int(t), 60)
    return f"{mins:02d}:{secs:02d}"


def ft_tqdm(lst: range) -> None:
    """A simple progress bar generator similar to tqdm.

    Displays a live progress bar in the terminal while iterating over a range.
    Shows the percentage, elapsed time, estimated remaining time, and speed.

    Args:
        lst: A range or iterable to loop through.

    Yields:
        Each item from the given iterable, one by one.

    Example:
        >>> for i in ft_tqdm(range(100)):
            ...     time.sleep(0.05)
    """
    total = len(lst)
    if (total == 0):
        print("0it [00:00, ?it/s]")
        return

    term_width = get_terminal_size().columns
    start_time = time.time()
    bar_width = max(10, term_width - 40)
    interval = 20
    for idx, item in enumerate(lst, start=1):
        percent = idx / total
        filled_len = int(bar_width * percent)
        bar = "█" * filled_len + " " * (bar_width - filled_len)

        elapsed = time.time() - start_time
        speed = idx / elapsed if elapsed > 0 else 0
        remaining = (total - idx) / speed if speed > 0 else 0

        elapsed_str = format_time(elapsed)
        remaining_str = format_time(remaining)

        line = f"{percent*100:3.0f}%|{bar}| {idx}/{total} " \
            f"[{elapsed_str}<{remaining_str}, {speed:6.2f}it/s]"
        if idx % interval == 0 or idx == total:
            if idx == 1:
                sys.stdout.write(line)
            else:
                sys.stdout.write("\r" + line)
            sys.stdout.flush()

        yield item

    bar = "█" * bar_width
    total_time = time.time() - start_time
    final_speed = total / total_time if total_time > 0 else 0
    line = f"100%|{bar}| {total}/{total} " \
        f"[{elapsed_str}<00:00, {final_speed:6.2f}it/s]"
    sys.stdout.write("\r" + line + "\n")
    sys.stdout.flush()
