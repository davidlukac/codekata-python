# A Needle in the Haystack
# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c


def find_needle(haystack: list) -> str:
    return 'found the needle at position %d' % haystack.index('needle')


def find_needle_5(haystack: list) -> str:
    return (lambda idx: {
        idx: 'found the needle at position %s' % idx,
        None: 'needle is not in the haystack',
    }.get(idx))(next((idx for idx, val in enumerate(haystack) if val == 'needle'), None))


def find_needle_4(haystack: list) -> str:
    idx = next((idx for idx, val in enumerate(haystack) if val == 'needle'), None)
    return 'found the needle at position %d' % idx if idx is not None else 'needle is not in the haystack'


def find_needle_3(haystack: list) -> str:
    return ("found the needle at position %s" % haystack.index(
        'needle')) if 'needle' in haystack else "needle is not in the haystack"


def find_needle_2(haystack: list) -> str:
    try:
        return "found the needle at position %s" % haystack.index('needle')
    except ValueError:
        return "needle is not in the haystack"


def find_needle_1(haystack: list) -> str:
    index = None

    try:
        index = haystack.index('needle')
    except ValueError:
        pass

    return ("found the needle at position %s" % index) if index is not None else "needle is not in the haystack"
