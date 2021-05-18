from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    # It should create the same hash with arguments of different data types
    # in any order
    assert crypto_hash(1, [2], 'three') == crypto_hash('three', 1, [2])
    assert crypto_hash('awe') == '614235e1d2ad3c1708aca284e3c3575cce543b749e0823dd63b49d003877739e'