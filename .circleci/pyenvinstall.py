import os
import subprocess


def main():
    target = '.'.join(os.environ['TOXENV'][-2:])
    versions = subprocess.check_output(
        ['pyenv', 'install', '--list'],
        encoding='utf-8',
    )
    versions = versions.splitlines()
    versions = [v.strip().split('.') for v in versions if 'dev' not in v]
    versions = [v for v in versions if '.'.join(v).startswith(target)]
    version = '.'.join(max(versions))
    subprocess.check_output(['pyenv', 'update'])
    subprocess.check_output(['pyenv', 'install', '--skip-existing', version])
    subprocess.check_output(['pyenv', 'global', version])


main()
