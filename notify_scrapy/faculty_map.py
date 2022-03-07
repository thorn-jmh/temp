import pdb
faculty_id = {
    'aeronautics':     1,
    'agriculture':     2,
    'animal':          3,
    'architecture':    4,
    'beis':            5, 
    'biosystems':      6,
    'career':          7,
    'chemistry':       8,
    'chu':             9,
    'cs':             10,
    'cse':            11,
    'danqing':        12,
    'earth':          13,
    'economics':      14,
    'electrical':     15,
    'energy':         16,
    'env':            17,
    'global':         18,
    'inter':          19,
    'isee':           20,
    'jwbinfo':        21,
    'lantian':        22,
    'law':            23,
    'library':        24,
    'life':           25,
    'logistics':      26,
    'marxism':        27,
    'materials':      28,
    'math':           29,
    'mechanical':     30,
    'media':          31,
    'medicine':       32,
    'optical':        33,
    'pharmaceutical': 34,
    'physics':        35,
    'polymer':        36,
    'psychology':     37,
    'public':         38,
    'qiushi':         39,
    'software':       40,
    'undergraduate':  41,
    'yunfeng':        42,
}


def key2value(key: str):
    if key not in faculty_id:
        print("AN err")
        return -1

    return faculty_id[key]
