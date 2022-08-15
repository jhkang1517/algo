def solution(s=''):
    dct = dict()
    dct['zero'] = '0'
    dct['one'] = '1'
    dct['two'] = '2'
    dct['three'] = '3'
    dct['four'] = '4'
    dct['five'] = '5'
    dct['six'] = '6'
    dct['seven'] = '7'
    dct['eight'] = '8'
    dct['nine'] = '9'

    for k, v in dct.items():
        s = s.replace(k, v)

    return int(s)
