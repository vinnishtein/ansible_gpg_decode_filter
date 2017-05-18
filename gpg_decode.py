import gnupg

def gpg_decode(encrypted_data):
    gpg = gnupg.GPG(gpgbinary='gpg2', use_agent=True)
    return gpg.decrypt(str(encrypted_data))

class FilterModule(object):
    ''' Ansible gpg decode variables filter with gpg agent '''

    def filters(self):
        filters = {
            'gpg_decode' : gpg_decode,
        }

        return filters
