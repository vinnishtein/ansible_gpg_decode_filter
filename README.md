# ansible_gpg_decode_filter
ansible plugin, allowing decrypt gpg data with jinja filters and gpg-agent

### Install plugin

```
$ pip install -r requirements.txt
$ sudo mkdir -p /usr/share/ansible/plugins/filter
$ cp gpg_decode.py /usr/share/ansible/plugins/filter/
```
### Generate gpg keypairs
```
$ gpg2 --full-gen-key
gpg (GnuPG) 2.1.11; Copyright (C) 2016 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: ansiblekey
Email address: 
Comment: 
You selected this USER-ID:
    "ansiblekey"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O

```
Ensure you have valid pinentry program, for asking passphrase
```
$ cat .gnupg/gpg-agent.conf 
default-cache-ttl 9999999
max-cache-ttl 9999999
pinentry-program /usr/bin/pinentry-curses

```
### Usage

Generate encrypted data
```
$ echo 'secretphrase' | gpg2 -a -e -r ansiblekey
-----BEGIN PGP MESSAGE-----
Version: GnuPG v2

hQIMA15sKcHFZoXVARAAlhAK51/uPep5xx9CYWWYQbfdiTYA5E5R2lOL4/eufqVT
zIk6FUWDymfIWRQCzMoH8R34STSst/SUU8OtCYQdmfD9Mb5aMO7ldYmhqlQgOtUM
5/jqtbikUGXsitmjtIyfVvpXxNClHnyFDGEjQyPvAf2sdFpwuVO+mM7hK8GtEMDZ
Y2lnduQqwh22EAesfuhDB4LDh3dCOqg4oZeUqtFP+YnBzo1o9HXikvll+BejnDLP
8UI1hPdpuhRwgXOZsHCHUnFIJ852iViyKdULEhFpaRJ0cEg/Fs9D7O1Mae5ACXLe
g6us3agWQOBQmhQwFihc5lZLxJbGGkJDr3A+iJUMiypJ/utBjVs+k5xMVClfWA+3
4ZuNdd7vrjp9Ux/I68A9oUQYyEue7aQoGWviukWc3nzk8XSLsv61s7TbF2MzcTsT
I58eUXUUfbaN4+qW/Rw0+io+SKKDlXpRcMfMlUAS0suhWKr86+YWj/rMHEKCohmh
pvp59K7HHsa9LGQpce+Ods6Xlnl4dt5QbJfm+xJwNYD2eLuOeZZi12Zz6nCgZcKy
K+OfQMeFwCHw9y7kNhaqS3g1BwgzZvZ9HtSgcP5a0Lb80n2Orkpg9YqPsSIGc2Fx
BvZTUVVmYJfMQKgzkUZaBbFBe2sFIO0Ssj5+1QNjtFCL9O4PXxsCO/FaKrh/OzjS
SAH6RYa4nNY3ZKZCevkamIPsfmJGuYOlkYu5tWDSFNi951Yl+bURDndsFTSrn7nH
o5fh8DBHmO6IF8Bw7UGOLBBYRTqsH41vbw==
=DavG
-----END PGP MESSAGE-----
```
Create minimal playbook:
```
- hosts: all
  vars:
    testvar: |
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v2

      hQIMA15sKcHFZoXVARAAlhAK51/uPep5xx9CYWWYQbfdiTYA5E5R2lOL4/eufqVT
      zIk6FUWDymfIWRQCzMoH8R34STSst/SUU8OtCYQdmfD9Mb5aMO7ldYmhqlQgOtUM
      5/jqtbikUGXsitmjtIyfVvpXxNClHnyFDGEjQyPvAf2sdFpwuVO+mM7hK8GtEMDZ
      Y2lnduQqwh22EAesfuhDB4LDh3dCOqg4oZeUqtFP+YnBzo1o9HXikvll+BejnDLP
      8UI1hPdpuhRwgXOZsHCHUnFIJ852iViyKdULEhFpaRJ0cEg/Fs9D7O1Mae5ACXLe
      g6us3agWQOBQmhQwFihc5lZLxJbGGkJDr3A+iJUMiypJ/utBjVs+k5xMVClfWA+3
      4ZuNdd7vrjp9Ux/I68A9oUQYyEue7aQoGWviukWc3nzk8XSLsv61s7TbF2MzcTsT
      I58eUXUUfbaN4+qW/Rw0+io+SKKDlXpRcMfMlUAS0suhWKr86+YWj/rMHEKCohmh
      pvp59K7HHsa9LGQpce+Ods6Xlnl4dt5QbJfm+xJwNYD2eLuOeZZi12Zz6nCgZcKy
      K+OfQMeFwCHw9y7kNhaqS3g1BwgzZvZ9HtSgcP5a0Lb80n2Orkpg9YqPsSIGc2Fx
      BvZTUVVmYJfMQKgzkUZaBbFBe2sFIO0Ssj5+1QNjtFCL9O4PXxsCO/FaKrh/OzjS
      SAH6RYa4nNY3ZKZCevkamIPsfmJGuYOlkYu5tWDSFNi951Yl+bURDndsFTSrn7nH
      o5fh8DBHmO6IF8Bw7UGOLBBYRTqsH41vbw==
      =DavG
      -----END PGP MESSAGE-----
  tasks:
    - name: template file
      template: src=test_template.txt  dest=/tmp/testfile.txt

```
Template file:
```
this is secret data: {{ testvar | gpg_decode }}
```
Launch playbook:
```
$ ansible-playbook testrole.yml -i hosts 

PLAY [all] ************************************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************************
ok: [localhost]

TASK [template file] **************************************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP ************************************************************************************************************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0   

$ cat /tmp/testfile.txt 
this is secret data: secretphrase

```
Now you can store passwords, and any other important data encrypted by your public key in public places like github
