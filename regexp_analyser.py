import re

types_list = [r'^int ', r'^short ', r'^long ']
name_re = r'^ ?[a-zA-Z][a-zA-Z0-9]{0,15}'

def to_normal_form(str):
    tmp = re.sub(r'^ {0,}', '', str)
    tmp = re.sub(r' +', ' ', tmp)
    tmp = re.sub(r' \(', '(', tmp)
    tmp = re.sub(r'\( ', '(', tmp)
    tmp = re.sub(r' \)', ')', tmp)
    tmp = re.sub(r' ;', ';', tmp)
    tmp = re.sub(r' ,', ',', tmp)
    tmp = re.sub(r', ', ',', tmp)
    return tmp

def analyze_type(str):
    for t in types_list:
        tmp = re.sub(t, '', str)
        if str != tmp:
            return  tmp, True
    else:
        return str, False



def analyze_part(str, template):
    tmp = re.sub(template, '', str)
    return tmp, tmp != str


def analyze(str):
    # print('------------------------------')

    normal = to_normal_form(str)
    # print(normal)
    tmp, correct = analyze_type(normal)
    if correct:
        tmp, correct = analyze_part(tmp, name_re)
        if correct:
            #TODO add save func name

            tmp, correct = analyze_part(tmp, r'^[(]')
            if correct:
                tmp, correct = analyze_part(tmp, r'[)];$')
                if correct:
                    while tmp:
                        # print ('1)   ' + tmp)
                        tmp, correct = analyze_type(tmp)
                        if not correct:
                            # print('param type error   ')
                            # break
                            return False
                        # print ('2)   ' + tmp)

                        tmp, correct = analyze_part(tmp, name_re)
                        if not correct:
                            # print('param name error')
                            # break
                            return False
                        # print ('3)   ' + tmp)

                        tmp, correct = analyze_part(tmp, r'[,]$')
                        if correct:
                            # print('param finish error')
                            # break
                            return False
                        else:
                            tmp = re.sub(r'^,','', tmp)
                    else:
                        # print("Correct")
                        return True
                else:
                    # print ('error in finish params')
                    return False
            else:
                # print('error in start params')
                return False
        else:
            # print('func name error')
            return False
    else:
        # print ("type error")
        return False
    # print('------------------------------')

if __name__ == '__main__':
    # analyze('   int    test123 ( int     b ,int   f )    ;')
    analyze('int DWva4DI09Wkzppa5   (long   pMQuCinz    ,int   BnQcWJYM3V ,long   gl5jYeAqIM3NIWZjL);')
    # analyze('   int    test_test12 ( int     b ,int   f )    ;')
    # analyze('int est123( intb ,int  f);')
    # analyze('int est123( int ,int  f);')
    # analyze('int est123( float c ,int  f);')
    # analyze('int est123( intb ,int  f)')
    # analyze('int a123)( int b ,int  f);')
    # analyze('int iAt();;')



