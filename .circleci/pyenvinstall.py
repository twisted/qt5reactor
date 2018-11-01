import os
import subprocess


def main():
    target = '.'.join(os.environ['TOXENV'][-2:])
    versions = subprocess.check_output(['pyenv', 'install', '--list'])
    versions = versions.splitlines()
    versions = [v.strip().split('.') for v in versions if 'dev' not in v]
    versions = [v for v in versions if '.'.join(v).startswith(target)]
    version = '.'.join(max(versions))
    subprocess.check_output(['pyenv', 'install', version])
    subprocess.check_output(['pyenv', 'global', version])


main()
