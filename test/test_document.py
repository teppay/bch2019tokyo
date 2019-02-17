#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import hashlib
import sha3
import subprocess
import binascii
import sys

from time import sleep

GETH_URL = 'http://localhost:8545'
DEVELOPPER_ETH_ADDR = '0x4aadec859f1501fdaf297978df81ba82bf178f72'

def test_document():
    with open('../data/sample_document_hash.json') as f:
        test_data = json.load(f)

    title = test_data['title']
    authors = test_data['authors']
    sentences = test_data['sentence']
    abstract = test_data['abstract']
    hash_function = 'FuzzyFunction'
    publishers = ['0x11eeed7eba60ed4774418e6cf2b64e4b1b00ccb4']

    print('[1/7] Creating document contract')
    doc_addr = document_contract_creation(title)
    if doc_addr:
        print(f'[1/7] Pass: address={doc_addr}')
    else:
        print('[1/7] Can\'t pass')
        sys.exit(1)

    # print('[2/7] Testing getTitle')
    # try:
    #     res = eth_responce2str(call_contract_view(doc_addr, 'getTitle()'))
    # except Exception as e:
    #     print(f'[2/7] Can\'t pass: {e}')
    #     sys.exit(1)
    # else:
    #     if res == title:
    #         print(f'[2/7] Pass')
    #     else:
    #         print('[2/7] Can\'t pass: wrong title')
    #         sys.exit(1)

    # print(f"[3/7] Testing setAuthor and getAuthor {authors}")
    # if test_document_set_get_author(doc_addr, authors):
    #     print(f"[3/7] Pass")
    # else:
    #     print('[3/7] Can\'t pass')
    #     sys.exit(1)

    # print(f"[4/7] Testing setSentence and getSentence {sentences}")
    # if test_document_set_get_sentence(doc_addr, sentences):
    #     print(f"[4/7] Pass")
    # else:
    #     print('[4/7] Can\'t pass')
    #     sys.exit(1)

    # print(f"[5/7] Testing setAbstarct and getAbstract {abstract}")
    # if test_document_set_get_abstract(doc_addr, abstract):
    #     print(f"[5/7] Pass")
    # else:
    #     print('[5/7] Can\'t pass')
    #     sys.exit(1)

    # print(f"[6/7] Testing setHashFunction and getHashFunction {hash_function}")
    # if test_document_set_get_hash_function(doc_addr, hash_function):
    #     print(f"[6/7] Pass")
    # else:
    #     print('[6/7] Can\'t pass')
    #     sys.exit(1)

    print(f"[7/7] Testing setPublisher and getPublisher {publishers}")
    if test_document_set_get_publisher(doc_addr, publishers):
        print(f"[7/7] Pass")
    else:
        print('[7/7] Can\'t pass')
        sys.exit(1)


def function2data(func):
    k = sha3.keccak_256()
    k.update(func.encode())
    return '0x' + k.hexdigest()[:8]



def document_contract_creation(title):
    subprocess.call(['./compile_document_sol.sh'])
    with open('./document.bin', 'r') as f:
        doc_bin = '0x'+f.read().strip()
    return create_document(doc_bin, title)

# stringをtransactionに乗せるhex形式に変換する
def str2eth_hex(s):
    data = ''
    length = len(s)
    data += format(0x20, '064x')
    data += format(length, '064x')
    fstr = '{:0<' + str((length//64 +1)*64)+ '}'
    data += fstr.format(binascii.hexlify(s.encode('utf-8')).decode('utf-8'))
    return data

def eth_responce2str(h):
    h = h.replace('0x', '')
    pointer = int(h[:64], 16)
    length = int(h[64:64*2], 16) * 2
    s = binascii.unhexlify(h[64*2:][:length])
    return s.decode('utf-8')

def create_document(doc_bin, title):
    data = ''
    data += doc_bin

    data += str2eth_hex(title)

    headers = {'Content-type': 'application/json'}
    payload = {'jsonrpc': '2.0',
               'method': 'eth_sendTransaction',
               'params':[{
                   'from': DEVELOPPER_ETH_ADDR,
                   'to': None,
                   'gas': hex(3000000),
                   'data': data
               }],
               'id': 1}
    res = requests.post(GETH_URL, headers=headers, json=payload)
    print(res.text)
    tx_hash = json.loads(res.text)['result']
    while True:
        try:
            return get_contract_addr(tx_hash)
        except:
            sleep(1)

def get_contract_addr(tx_hash):
    headers = {'Content-type': 'application/json'}
    payload = {'jsonrpc': '2.0',
               'method': 'eth_getTransactionReceipt',
               'params':[tx_hash],
               'id': 1}

    res = requests.post(GETH_URL, headers=headers, json=payload)
    return json.loads(res.text)['result']['contractAddress']

def call_contract_view(addr, func, arg=None):
    headers = {'Content-type': 'application/json'}

    data = ''
    data += function2data(func)
    if arg != None:
        if type(arg) == int:
            data += format(arg, '064x')
        elif type(arg) == str:
            data += str2eth_hex(arg)

    payload = {'jsonrpc': '2.0',
               'method': 'eth_call',
               'params':[{'from': DEVELOPPER_ETH_ADDR, 'to': addr, 'data': data}, 'latest'],
               'id': 1}
    res = requests.post(GETH_URL, headers=headers, json=payload)
    print(addr, func, arg,res.text)
    ret = json.loads(res.text)['result']
    return ret

def call_contract_sendTransaction(addr, func, arg=None):
    headers = {'Content-type': 'application/json'}
    print('arg',arg)

    data = ''
    data += function2data(func)
    if arg != None:
        if type(arg) == int:
            data += format(arg, '064x')
        elif arg.startswith('0x'):
            data += format(int(arg, 16), '064x')
            print(data)
        elif type(arg) == str:
            data += str2eth_hex(arg)

    payload = {'jsonrpc': '2.0',
               'method': 'eth_sendTransaction',
               'params':[{'from': DEVELOPPER_ETH_ADDR, 'to': addr, 'data': data, 'gas': hex(3000000)}],
               'id': 1}
    res = requests.post(GETH_URL, headers=headers, json=payload)
    print(addr, func, arg,res.text)
    ret = json.loads(res.text)['result']
    return ret

def test_document_set_get_author(doc_addr, authors):
    initial_pending = get_num_pendingTx(DEVELOPPER_ETH_ADDR)
    for idx in range(len(authors)):
        call_contract_sendTransaction(doc_addr, 'setAuthor(string)', arg=authors[idx])

    # Txが全部ブロックに入るのを待つ
    while (get_num_pendingTx(DEVELOPPER_ETH_ADDR) - initial_pending) > 0:
        print('.', end='')
        sleep(1)

    n = int(call_contract_view(doc_addr, 'getNumOfAuthors()'), 16)
    print(n)
    while n < len(authors):
        sleep(1)
        n = int(call_contract_view(doc_addr, 'getNumOfAuthors()'), 16)
        print(n)

    for idx in range(len(authors)):
        a = eth_responce2str(call_contract_view(doc_addr, 'getAuthor(uint256)', arg=idx))
        if a != authors[idx]:
            return False
    return True

def test_document_set_get_sentence(doc_addr, sentences):
    initial_pending = get_num_pendingTx(DEVELOPPER_ETH_ADDR)
    for idx in range(len(sentences)):
        call_contract_sendTransaction(doc_addr, 'setSentence(string)', arg=sentences[idx])

    # Txが全部ブロックに入るのを待つ
    while (get_num_pendingTx(DEVELOPPER_ETH_ADDR) - initial_pending) > 0:
        print('.', end='')
        sleep(1)

    n = int(call_contract_view(doc_addr, 'getNumOfSentences()'), 16)
    print(n)
    while n < len(sentences):
        sleep(1)
        n = int(call_contract_view(doc_addr, 'getNumOfSentences()'), 16)
        print(n)

    for idx in range(len(sentences)):
        s = eth_responce2str(call_contract_view(doc_addr, 'getSentence(uint256)', arg=idx))
        if s != sentences[idx]:
            return False
    return True

def test_document_set_get_abstract(doc_addr, abstract):
    initial_pending = get_num_pendingTx(DEVELOPPER_ETH_ADDR)
    for idx in range(len(abstract)):
        call_contract_sendTransaction(doc_addr, 'setAbstract(string)', arg=abstract[idx])

    # Txが全部ブロックに入るのを待つ
    while (get_num_pendingTx(DEVELOPPER_ETH_ADDR) - initial_pending) > 0:
        print('.', end='')
        sleep(1)

    n = int(call_contract_view(doc_addr, 'getNumOfAbstract()'), 16)
    print(n)
    while n < len(abstract):
        sleep(1)
        n = int(call_contract_view(doc_addr, 'getNumOfAbstract()'), 16)
        print(n)

    for idx in range(len(abstract)):
        s = eth_responce2str(call_contract_view(doc_addr, 'getAbstract(uint256)', arg=idx))
        if s != abstract[idx]:
            return False
    return True

def test_document_set_get_hash_function(doc_addr, hash_function):
    call_contract_sendTransaction(doc_addr, 'setHashFunction(string)', arg=hash_function)
    while True:
        h = eth_responce2str(call_contract_view(doc_addr, 'getHashFunction()'))
        print(h, hash_function)
        sleep(1)
        if h == hash_function:
            break
    return True

def test_document_set_get_publisher(doc_addr, publishers):
    initial_pending = get_num_pendingTx(DEVELOPPER_ETH_ADDR)
    for idx in range(len(publishers)):
        call_contract_sendTransaction(doc_addr, 'setPublisher(string)', arg=publishers[idx])

    # Txが全部ブロックに入るのを待つ
    while (get_num_pendingTx(DEVELOPPER_ETH_ADDR) - initial_pending) > 0:
        print('.', end='')
        sleep(1)

    n = int(call_contract_view(doc_addr, 'getNumOfPublishers()'), 16)
    print(n)
    while n < len(publishers):
        sleep(1)
        n = int(call_contract_view(doc_addr, 'getNumOfPublishers()'), 16)
        print(n)

    for idx in range(len(publishers)):
        s = eth_responce2str(call_contract_view(doc_addr, 'getPublisher(uint256)', arg=idx))
        if s != publishers[idx]:
            return False
    return True

def get_num_pendingTx(addr):
    headers = {'Content-type': 'application/json'}
    payload = {'jsonrpc': '2.0',
               'method': 'eth_getTransactionCount',
               'params':[addr,
                         'pending'],
               'id': 1}
    res = requests.post(GETH_URL, headers=headers, json=payload)
    p = int(json.loads(res.text)['result'], 16)
    print(p)
    return p


if __name__ == '__main__':
    test_document()