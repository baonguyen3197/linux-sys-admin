# Use Python REPL
``python``
python3
>>> import subprocess
>>> proc = subprocess.run(['ls', '-l'])
total 8
-rw-r--r-- 1 user user  0 Jun 15 12:00 file1.txt
-rw-r--r-- 1 user user  0 Jun 15 12:00 file2.txt
>>> proc
CompletedProcess(args=['ls', '-l'], returncode=0)
>>> proc.returncode
0
>>> proc.args
['ls', '-l']    
>>> proc = subprocess.run(
    ['ls', '-l',],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
>>> proc
CompletedProcess(args=['ls', '-l'], returncode=0, stdout=b'total 8\n-rw-r--r-- 1 user user  0 Jun 15 12:00 file1.txt\n-rw-r--r-- 1 user user  0 Jun 15 12:00 file2.txt\n', stderr=b'')
>>> proc.stdout
b'total 8\n-rw-r--r-- 1 user user  0 Jun 15 12:00 file1.txt\n-rw-r--r-- 1 user user  0 Jun 15 12:00 file2.txt\n'
>>> print(proc.stdout)
b'total 8\n-rw-r--r-- 1 user user  0 Jun 15 12:00 file1.txt\n-rw-r--r-- 1 user user  0 Jun 15 12:00 file2.txt\n'
>>> bytes([46, 46, 46])
b'...'
>>> bytes([255, 1, 0])
b'\xff\x01\x00'
>>> print(proc.stdout.decode())
total 8
-rw-r--r-- 1 user user  0 Jun 15 12:00 file1.txt
-rw-r--r-- 1 user user  0 Jun 15 12:00 file2.txt
>>> new_proc = subprocess.run(['cat', 'fake.txt'])
cat: fake.txt: No such file or directory
>>> new_proc
CompletedProcess(args=['cat', 'fake.txt'], returncode=1)
>>> new_proc = subprocess.run(['cat', 'fake.txt'], check=True)
cat: fake.txt: No such file or directory
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/subprocess.py", line 493, in run
    raise CalledProcessError(retcode, process.args, output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['cat', 'fake.txt']' returned non-zero exit status 1.
>>> 