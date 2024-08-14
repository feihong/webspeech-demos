import subprocess
import shutil
from pathlib import Path

build_dir = Path('_build')

if not build_dir.exists():
  build_dir.mkdir()

for html_file in Path('.').glob('*.html'):
  shutil.copy(html_file, build_dir)

cmd = [
  'ghp-import',
  '--no-jekyll',
  '--push',
  '--no-history',
  build_dir
]
subprocess.run(cmd)

print(f'Deployed to https://feihong.github.io/webspeech-demos/')
