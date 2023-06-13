def SET_BIT(REG,BIT_NO):
    REG |= (1<<BIT_NO)
    return REG

def CLEAR_BIT(REG,BIT_NO):
    REG &= ~(1<<BIT_NO)
    return REG

def GET_BIT(REG,BIT_NO):
    (REG>>BIT_NO) & 1
    return REG

def TOGGLE_BIT(REG,BIT_NO):
    REG ^= (1<<BIT_NO)
    return REG
