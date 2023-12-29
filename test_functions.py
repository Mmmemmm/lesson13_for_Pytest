from functions import salary,hello_who

def test_who_max():
    assert hello_who('Max')=='Hello,Max'

def test_who_2():
    assert hello_who(123) == 'Hello,123'
    assert hello_who('bebra')=='Hello,bebra'
    assert hello_who(24322353535)=='Hello التفاح المجفف بنكهة الزنجبيل'
    assert hello_who('skibidi toilet')=='Hello,brrrrrrrrrrs skibidi dop dop dop es es'