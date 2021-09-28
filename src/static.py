import requests
import argparse
import urllib.parse
import shutil

from .questions import questions
from .path import get_path_from_root
from .static_search import prepare_static_search

parser = argparse.ArgumentParser(description='Make a static copy of the data from the API')
parser.add_argument(
  '--server',
  default='http://localhost:8000',
  help='URL of the server hosting the API',
)
args = parser.parse_args()

out_folder = get_path_from_root('static')
shutil.rmtree(str(out_folder), ignore_errors=True)
out_folder.mkdir()
(out_folder / "answer").mkdir()

def get_url(relative_path):
  return urllib.parse.urljoin(args.server, relative_path)

def get_and_save(path: str):
  assert not path.startswith('/')
  assert not path.startswith('.')

  print('saving', path)
  r = requests.get(get_url('/' + path))
  r.raise_for_status()
  (out_folder / path).write_bytes(r.content)

get_and_save('questions')

for q in questions:
  get_and_save(f"answer/{q['id']}")

(out_folder / "search").mkdir()
prepare_static_search(out_folder / "search")