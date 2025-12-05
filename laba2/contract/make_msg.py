from tonsdk.boc import begin_cell #для деплоя

def make_msg_body():
    return begin_cell().store_uint(1, 32).end_cell()

if __name__ == '__main__':
    print(make_msg_body())