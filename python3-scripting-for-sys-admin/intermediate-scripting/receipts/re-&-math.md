# Use Python REPL
``python``
python3
>>> import glob
>>> receipts = glob.glob('./new/receipt-[0-9]*[24680].json')
>>> receipts
['./new/receipt-10.json', './new/receipt-14.json', './new/receipt-14.json', './new/receipt-16.json', './new/receipt-18.json']
>>> import re
>>> re.match('./new/receipt-[0-9]*[24680].json', './new/receipt-2.json')
<_sre.SRE_Match object; span=(0, 26), match='./new/receipt-2.json'>
>>> bool(re.match('./new/receipt-[0-9]*[24680].json', './new/receipt-2.json'))
True
>>> receipt = [f for f in glob.glob('./new/receipt-[0-9]*.json') if re.match('./new/receipt-[0-9]*[24680].json', f)]
>>> receipt
['./new/receipt-10.json', './new/receipt-14.json', './new/receipt-14.json', './new/receipt-16.json', './new/receipt-18.json', './new/receipt-2.json', './new/receipt-4.json', './new/receipt-0.json']
>>> 