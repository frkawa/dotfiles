#!/usr/bin/env python3
"""Pattern 4: Fine-grained progress bar with true color gradient"""
import json, sys, time
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

data = json.load(sys.stdin)

BLOCKS = ' ▏▎▍▌▋▊▉█'
R = '\033[0m'
DIM = '\033[2m'

def gradient(pct):
    if pct < 50:
        r = int(pct * 5.1)
        return f'\033[38;2;{r};200;80m'
    else:
        g = int(200 - (pct - 50) * 4)
        return f'\033[38;2;255;{max(g,0)};60m'

def bar(pct, width=10):
    pct = min(max(pct, 0), 100)
    filled = pct * width / 100
    full = int(filled)
    frac = int((filled - full) * 8)
    b = '█' * full
    if full < width:
        b += BLOCKS[frac]
        b += '░' * (width - full - 1)
    return b

def remaining_hm(resets_at):
    """Return 'あとXh Ym' style string (hours + minutes)."""
    secs = max(0, int(resets_at) - int(time.time()))
    h, m = divmod(secs // 60, 60)
    if h > 0:
        return f'あと{h}時間{m}分'
    return f'あと{m}分'

def remaining_h(resets_at):
    """Return 'あとXh' style string (hours only)."""
    secs = max(0, int(resets_at) - int(time.time()))
    h = secs // 3600
    return f'あと{h}時間'

def fmt(label, pct, reset_str=None):
    p = round(pct)
    base = f'{label} {gradient(pct)}{bar(pct)} {p}%{R}'
    if reset_str:
        base += f' {DIM}{reset_str}{R}'
    return base

model = data.get('model', {}).get('display_name', 'Claude')
parts = [model]

ctx = data.get('context_window', {}).get('used_percentage')
if ctx is not None:
    parts.append(fmt('ctx', ctx))

five_data = data.get('rate_limits', {}).get('five_hour', {})
five = five_data.get('used_percentage')
if five is not None:
    resets_at = five_data.get('resets_at')
    reset_str = remaining_hm(resets_at) if resets_at else None
    parts.append(fmt('5h', five, reset_str))

week_data = data.get('rate_limits', {}).get('seven_day', {})
week = week_data.get('used_percentage')
if week is not None:
    resets_at = week_data.get('resets_at')
    reset_str = remaining_h(resets_at) if resets_at else None
    parts.append(fmt('7d', week, reset_str))

print(f'{DIM}│{R}'.join(f' {p} ' for p in parts), end='')
