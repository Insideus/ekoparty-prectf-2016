known = {
    0: 'E',
    1: 'K',
    2: 'O',
    3: '{',
    17: '}',
}

equation = [
    (13, 14, 0xcb),
    (13, 12, 0xcf),
    (10, 11, 0xc3),
    (8, 9, 0xd4),
    (12, 11, 0xc9),
    (15, 14, 0xd7),
    (5, 6, 0xd9),
    (10, 9, 0xc3),
    (4, 5, 0xe9),
    (3, 4, 0xf1),
    (16, 17, 0xf2),
    (1, 2, 0x9a),
    (3, 2, 0xca),
    (7, 6, 0xda),
    (7, 8, 0xe4),
    (16, 15, 0xeb),
]

while len(known) < 17:
    for a, b, total in equation:
        if a in known and b in known:
            continue

        if a in known:
            known[b] = chr(total - ord(known[a]))
        elif b in known:
            known[a] = chr(total - ord(known[b]))

print "".join(c for i, c in sorted(known.items()))
